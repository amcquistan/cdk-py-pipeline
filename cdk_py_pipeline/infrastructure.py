from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    CfnOutput,
    Stack,
    Stage,
)


class InfrastructureStack(Stack):
  vpc_id: CfnOutput
  fargate_cluster_arn: CfnOutput

  def __init__(self, scope: Construct, construct_id: str, **kwargs):
    super().__init__(scope, construct_id, **kwargs)

    vpc = ec2.Vpc(self, "vpc", max_azs=2)
    fargate_cluster = ecs.Cluster(self, "fargate-cluster", vpc=vpc)

    self.vpc_id = CfnOutput(self, "vpc-id", value=vpc.vpc_id)
    self.fargate_cluster_arn = CfnOutput(self, "fargate-cluster-arn", value=fargate_cluster.cluster_arn)


class InfrastructureStage(Stage):
  vpc_id: CfnOutput
  fargate_cluster_arn: CfnOutput

  def __init__(self, scope: Construct, construct_id: str, **kwargs):
    super().__init__(scope, construct_id, **kwargs)

    stack = InfrastructureStack(self, "infra-stack", **kwargs)

    self.vpc_id = stack.vpc_id
    self.fargate_cluster_arn = stack.fargate_cluster_arn
