#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from pipeline.pipeline_stack import PipelineStack

from aws_cdk import core


app = core.App()

pl = PipelineStack(app, 'PipelineStack', env={
    "account": "555618984259",
    "region": "us-east-1"
})

core.Tags.of(pl).add("Project", "cdkdemo")

app.synth()




