from aws_cdk import core, aws_codepipeline as codepipeline, aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
from aws_cdk import aws_codecommit as codecommit

from serverless_stage import ApplicationDevStage, ApplicationProdStage
from cdk_config.deployment_env import aws_account_info


class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        # Source
        # source_action = cpactions.GitHubSourceAction(
        #     action_name="Github",
        #     output=source_artifact,
        #     oauth_token=core.SecretValue.secrets_manager("cdk/githubtoken"),
        #     owner="ishan-aws",
        #     repo="cdk-pipelines-demo",
        #     trigger=cpactions.GitHubTrigger.POLL
        # )

        # Source
        repo = codecommit.Repository(self, "CodeRepo", repository_name="cdkworkshop")
        source_action = cpactions.CodeCommitSourceAction(
            action_name="CodeCommit",
            output=source_artifact,
            repository=repo,
            branch="withdocs"
        )

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

        dev_stage = ApplicationDevStage(self, 'ApplicationDevStage')
        pipeline_dev_stage = pipeline.add_application_stage(dev_stage)
        pipeline_dev_stage.add_manual_approval_action()

        prod_stage = ApplicationProdStage(self, 'ApplicationProdStage')
        pipeline.add_application_stage(prod_stage)
