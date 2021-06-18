+++
title = "Manual Approval"
weight = 80
+++

![](/30-pipeline/80-complete-pipeline-stage/pipeline_manual.png)

Let's now add the manual review flow. 

This can be done modifying `pipeline_stack.py` to include
```python
pipeline_dev_stage.add_manual_approval_action()
```

-----
-----


The completed `pipeline_stack.py` should look like

```python
from aws_cdk import core, aws_codepipeline as codepipeline, aws_codepipeline_actions as cpactions
from aws_cdk import pipelines

from .serverless_stage import ApplicationDevStage, ApplicationProdStage

deployment_env = {
    "account": "__YOUR__ACCOUNT__ID__",
    "region": "ap-southeast-2"
}


class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        # Source
        source_action = cpactions.CodeCommitSourceAction(
            action_name="CodeCommit",
            output=source_artifact,
            repository="__REPLACE__WITH__ARN__",
        )
        
        # source_action = cpactions.GitHubSourceAction(
        #     action_name="Github",
        #     output=source_artifact,
        #     oauth_token=core.SecretValue.secrets_manager("cdk/githubtoken"),
        #     owner="----",
        #     repo="cdk-pipelines-demo",
        #     trigger=cpactions.GitHubTrigger.POLL
        # )

        # Synthesise
        synth_action = pipelines.SimpleSynthAction(
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_assembly_artifact,
            install_command="npm install -g aws-cdk && pip install -r requirements.txt",
            synth_command="cdk synth"
        )

        # Create the pipeline
        pipeline = pipelines.CdkPipeline(self, "Pipeline",
                                         cloud_assembly_artifact=cloud_assembly_artifact,
                                         pipeline_name="ServerlessPipeline",
                                         source_action=source_action,
                                         synth_action=synth_action)

        dev_stage = ApplicationDevStage(self, 'ApplicationDevStage', env=deployment_env)
        pipeline_dev_stage = pipeline.add_application_stage(dev_stage)
        pipeline_dev_stage.add_manual_approval_action()

        prod_stage = ApplicationProdStage(self, 'ApplicationProdStage', env=deployment_env)
        pipeline.add_application_stage(prod_stage)
```