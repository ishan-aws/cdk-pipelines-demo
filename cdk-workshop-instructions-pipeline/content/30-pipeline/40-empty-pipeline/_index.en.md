+++
title = "Basic Pipeline"
weight = 40
+++

We can now complete defining our Pipeline. The basic pipeline has two stages defined;
* Source 
* Synthesize

```python
# Create the pipeline
pipeline = pipelines.CdkPipeline(self, "Pipeline",
                                 cloud_assembly_artifact=cloud_assembly_artifact,
                                 pipeline_name="ServerlessPipeline",
                                 source_action=source_action,
                                 synth_action=synth_action)
```

-----
-----

The `pipeline_stack.py` file should look like this

```python
class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        # Source
        source_action = cpactions.CodeCommitSourceAction(
            action_name="CodeCommit",
            output=source_artifact,
            repository="__ARN__OF__CODECOMMIT__REPO__",
        )
        
        # Synthesise
        synth_action = pipelines.SimpleSynthAction(
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_assembly_artifact,
            install_command="npm install -g aws-cdk && pip install -r requirements.txt",
            synth_command="cdk synth"
        )
        
        # Pipeline
        pipeline = pipelines.CdkPipeline(self, "Pipeline",
                                                 cloud_assembly_artifact=cloud_assembly_artifact,
                                                 pipeline_name="ServerlessPipeline",
                                                 source_action=source_action,
                                                 synth_action=synth_action)
                
```
