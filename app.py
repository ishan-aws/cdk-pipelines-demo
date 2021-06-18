#!/usr/bin/env python3
from aws_cdk import core
from cdk_config.deployment_env import aws_account_info

from pipeline.demo_api import LambdaApiDev, LambdaApiProd

##########
# TODO: change the aws_account_info in `cdk_config/deployment_env.py` file
##########

app = core.App()

dev_stack = LambdaApiDev(app, "LambdaApiDev", env=aws_account_info)
prod_stack = LambdaApiProd(app, "LambdaApiProd", env=aws_account_info)

app.synth()
