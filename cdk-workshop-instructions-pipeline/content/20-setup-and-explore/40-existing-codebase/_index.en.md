+++
title = "Starter Codebase Description"
weight = 30
+++

There are two key files in the codebase that are provided.

### Stack Definition
In the file `pipeline/serverless_function.py` you can find the stack defined. 

```python
from aws_cdk import core, aws_codedeploy as codedeploy, aws_lambda as _lambda, aws_apigateway as apig

from os import path

this_dir = path.dirname(__file__)


class LambdaApiDev(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs):
        super().__init__(app, id, **kwargs)

        lambda_code = _lambda.Code.from_asset(path.join(this_dir, "lambda"))

        self.func = _lambda.Function(self, "LambdaDev", code=lambda_code,
                                     handler="handler.handler",
                                     runtime=_lambda.Runtime.PYTHON_3_7)

        self.api = apig.LambdaRestApi(self, "SampleApi-Dev", handler=self.func,
                                      deploy_options=apig.StageOptions(
                                          stage_name="v1"
                                      ))
```


The above code defines a Lambda function running in the Python 3.7 enviornment with the default options. 

An API is created using APIGateway that allows the created Lambda function to handle the request.

### Stack Deployment
The `app.py` is where the two different environment stacks are created. 

```python
from pipeline.serverless_function import LambdaApiDev, LambdaApiProd

from aws_cdk import core

app = core.App()

LambdaApiDev(app, 'LambdaApiDev')
LambdaApiProd(app, 'LambdaApiProd')

app.synth()
```

`LambdaApiProd` class definition can also be found in `pipeline/serverless_function`

Running `cdk deploy` inside the directory would deploy two different stacks.


### Who, How?

Q: Who runs the `cdk deploy` command?

A: An automated code pipeline will run it whenever new code is pushed to Git.
