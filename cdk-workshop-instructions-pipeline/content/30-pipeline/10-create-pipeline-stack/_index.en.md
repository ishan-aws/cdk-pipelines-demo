+++
title = "Define Pipeline Stack"
weight = 10
+++


We can begin by creating a new file named `pipeline_stack.py` in the `pipeline` folder. 

Add the following lines of code to the file.

```python
from aws_cdk import core, aws_codepipeline as codepipeline, aws_codepipeline_actions as cpactions
from aws_cdk import pipelines

deployment_env = {
    "account": "YOUR_ACCOUNT_ID",
    "region": "ap-southeast-2"
}

```
The code above is importing the required `aws_cdk` modules required to create a pipeline. 

The `deployment_env` defines the account and region that the pipeline will deploy into. 

_Please replace the `YOUR_ACCOUNT_ID` with the correct value_

-----

Now let us make the Pipeline Stack.

```python
class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()
```

The `source_artifact` and `cloud_assembly_artifact` will be used by the pipeline.

