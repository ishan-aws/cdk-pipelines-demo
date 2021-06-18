#!/usr/bin/env python3
from aws_cdk import core

from pipeline.demo_api import LambdaApiDev, LambdaApiProd

app = core.App()

dev_stack = LambdaApiDev(app, "LambdaApiDev")
prod_stack = LambdaApiProd(app, "LambdaApiProd")

app.synth()
