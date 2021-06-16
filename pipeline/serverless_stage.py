from aws_cdk import core, aws_apigateway as apig
from .serverless_function import LambdaStackWithApi


class ServerlessStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, flavour: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        service = LambdaStackWithApi(self, 'DevServerlessFunction'+flavour, stage=flavour)
