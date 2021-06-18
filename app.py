#!/usr/bin/env python3
from aws_cdk import core
from cdk_config.deployment_env import aws_account_info

from pipeline.pipeline_stack import PipelineStack

app = core.App()

PipelineStack(app, 'PipelineStack', env=aws_account_info)

app.synth()
