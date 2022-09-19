import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_py_pipeline.infrastructure import InfrastructureStack


def test_create_infra_vpc():
    app = core.App()
    stack = InfrastructureStack(app, "stack")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::EC2::VPC", 1)


def test_create_infra_fargate_cluster():
    app = core.App()
    stack = InfrastructureStack(app, "stack")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::ECS::Cluster", 1)
