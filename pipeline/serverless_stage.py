from aws_cdk import core
from aws_cdk.aws_codepipeline import IStage
from .serverless_function import LambdaStack


class ServerlessStage(IStage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        service = LambdaStack(self, 'ServerlessFunction')
        self.output = service.fn_name
