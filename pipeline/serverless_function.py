from aws_cdk import core, aws_codedeploy as codedeploy, aws_lambda as _lambda, aws_apigateway as apig

from os import path


class LambdaStackWithApi(core.Stack):
    def __init__(self, app: core.App, id: str, stage: str = "dev", **kwargs):
        super().__init__(app, id, **kwargs)

        this_dir = path.dirname(__file__)
        self.lambda_code = _lambda.Code.from_asset(path.join(this_dir, "lambda"))
        self.func = _lambda.Function(
            self,
            "Lambda" + stage,
            code=self.lambda_code,
            handler="handler.handler",
            runtime=_lambda.Runtime.PYTHON_3_7
        )

        self.api = apig.LambdaRestApi(self, "APIGwAPI", handler=self.func,
                                      deploy_options=apig.StageOptions(
                                          stage_name=stage
                                      ))

        self.info = core.CfnOutput(self, f"APIURL+{stage}", value=self.api.url)
