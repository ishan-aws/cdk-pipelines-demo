from aws_cdk import core, aws_codedeploy as codedeploy, aws_lambda as _lambda, aws_apigateway as apig

from os import path


class LambdaStackWithApi(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs):
        super().__init__(app, id, **kwargs)

        this_dir = path.dirname(__file__)
        self.lambda_code = _lambda.Code.from_asset(path.join(this_dir, "lambda"))
        self.func = _lambda.Function(
            self,
            "Lambda",
            code=self.lambda_code,
            handler="handler.handler",
            runtime=_lambda.Runtime.PYTHON_3_7
        )

        self.api = apig.LambdaRestApi(self, "APIGwAPI", handler=self.func,
                                      deploy=False)
        self.deployment = apig.Deployment(self, 'Deployment', api=self.api)
        self.get_dev_api_stage()
        self.get_prod_api_stage()

    def get_dev_api_stage(self):
        return apig.Stage(self, 'APIGStage-Dev', deployment=self.deployment, stage_name="dev")

    def get_prod_api_stage(self):
        return apig.Stage(self, 'APIGStage-Prod', deployment=self.deployment, stage_name="prod")

        # self.info = core.CfnOutput(self, f"APIURL+{stage}", value=self.api.url)
