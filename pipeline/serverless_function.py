from aws_cdk import core, aws_codedeploy as codedeploy, aws_lambda as _lambda
from os import path


class LambdaStack(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs):
        super().__init__(app, id, **kwargs)

        this_dir = path.dirname(__file__)
        self.lambda_code = _lambda.Code.from_asset(path.join(this_dir, "lambda"))
        func = _lambda.Function(
            self,
            "Lambda",
            code=self.lambda_code,
            handler="handler.handler",
            runtime=_lambda.Runtime.PYTHON_3_7
        )

        alias = _lambda.Alias(self, "HandlerAlias",
                              alias_name="Current",
                              version=func.current_version)

        codedeploy.LambdaDeploymentGroup(self, "DeploymentGroup",
                                         alias=alias,
                                         deployment_config=codedeploy.LambdaDeploymentConfig.ALL_AT_ONCE)

        self.fn_name = core.CfnOutput(self, "Url", value=func.function_name)
