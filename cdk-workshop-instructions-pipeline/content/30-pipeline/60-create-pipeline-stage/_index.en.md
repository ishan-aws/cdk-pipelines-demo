+++
title = "User Defined Stages"
weight = 60
+++

![](/30-pipeline/60-create-pipeline-stage/pipeline_user_stages.png)

Let's make a stage for our API Deployment

We can begin by creating a new file named `serverless_stage.py` in the `pipeline` folder.

Add the code below to the file

```python
from aws_cdk import core

from .serverless_function import LambdaApiDev, LambdaApiProd


class ApplicationDevStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.service = LambdaApiDev(self, 'ApplicationDevStage')
```

The `ApplicationDevStage` can be added to the pipeline. The stage provisions the `LambdaApiDev` stack which consists of APIGateway + Lambda.

You can add one or more stacks to a given stage. 

-----
-----

Now create a **production stage** by adding the following lines to the `serverless_stage.py` file. 

```python
class ApplicationProdStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.service = LambdaApiProd(self, 'ApplicationProdStage')

```

Notice it is using the `LambdaApiProd` stack, which provides higher memory capacity to the provisioned Lambdas.

-----
-----

The stage is now set!