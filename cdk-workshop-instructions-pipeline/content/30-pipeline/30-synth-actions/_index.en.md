+++
title = "Build Action"
weight = 30
+++

![](/30-pipeline/30-synth-actions/pipeline_build.png)

To deploy the CDK Stacks, our pipeline must be able to synthesize the CDK stacks. 

In order to facilitate this, a synth_action can be created as follows

The synth action can be run with CDK tool. Before it can be run, it has to fetch all the dependencies for the Python code. 
Those can be run as `install_command` which is run before the `synth_command`


```python
# Synthesise
synth_action = pipelines.SimpleSynthAction(
    source_artifact=source_artifact,
    cloud_assembly_artifact=cloud_assembly_artifact,
    install_command="npm install -g aws-cdk && pip install -r requirements.txt",
    synth_command="cdk synth"
)
```

Add the synth action `synth_action` to the `pipeline_stack.py` file.

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
```
