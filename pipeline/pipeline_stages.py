from aws_cdk import core

from .demo_api import LambdaApiDev, LambdaApiProd


class ApplicationDevStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.service = LambdaApiDev(self, 'ApplicationDevStage')


class ApplicationProdStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.service = LambdaApiProd(self, 'ApplicationProdStage')
