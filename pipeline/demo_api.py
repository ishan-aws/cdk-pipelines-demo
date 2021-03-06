from os import path

from aws_cdk import core, aws_lambda as _lambda, aws_apigateway as apig

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

        core.CfnOutput(self, "DevFuncArn", value=self.func.function_name)
        core.CfnOutput(self, "DevApiEndpoint", value=self.api.url)


class LambdaApiProd(core.Stack):
    """
    A more powerful lambda configuration, with 1GB Memory.
    """
    def __init__(self, app: core.App, id: str, **kwargs):
        super().__init__(app, id, **kwargs)

        lambda_code = _lambda.Code.from_asset(path.join(this_dir, "lambda"))

        self.func = _lambda.Function(self, "LambdaProd", code=lambda_code,
                                     handler="handler.handler",
                                     runtime=_lambda.Runtime.PYTHON_3_7, memory_size=1024)

        self.api = apig.LambdaRestApi(self, "SampleApi-Prod", handler=self.func, deploy_options=apig.StageOptions(
            stage_name="v1"
        ))

        core.CfnOutput(self, "ProdFuncArn", value=self.func.function_name)
        core.CfnOutput(self, "ProdApiEndpoint", value=self.api.url)
