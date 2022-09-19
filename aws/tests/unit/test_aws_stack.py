import aws_cdk as core
import aws_cdk.assertions as assertions
from aws.aws_stack import PipelineStack


def test_pipeline_created():
    app = core.App()
    stack = PipelineStack(app, "aws", connection_arn="faked")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::CodePipeline::Pipeline", 1)
