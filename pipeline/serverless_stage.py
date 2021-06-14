from aws_cdk import core
from .serverless_function import LambdaStack


class ServerlessStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        service = LambdaStack(self, 'ServerlessFunction')
        self.output = service.fn_name
