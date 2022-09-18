#!/usr/bin/env python3

import aws_cdk as cdk

from aws.aws_stack import PipelineStack


app = cdk.App()
PipelineStack(app, "pipeline",
  connection_arn="arn:aws:codestar-connections:us-east-1:180847865862:connection/3f9f0372-2d5e-4e81-a4c5-c3c0446d401a",
  stack_name="cdk-py-pipeline"
)

app.synth()
