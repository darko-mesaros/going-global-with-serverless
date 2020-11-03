#!/usr/bin/env python3

from aws_cdk import core

from going_global_with_serverless.going_global_with_serverless_stack import GoingGlobalWithServerlessStack


app = core.App()
GoingGlobalWithServerlessStack(app, "going-global-with-serverless")

app.synth()
