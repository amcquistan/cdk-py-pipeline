from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines
)

from cdk_py_pipeline.infrastructure import InfrastructureStage


class CdkPyPipelineStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, connection_arn: str, **kwargs):
    super().__init__(scope, construct_id, **kwargs)
    
    # source code location referenced via GitHub Connection
    source = pipelines.CodePipelineSource.connection(
      repo_string="amcquistan/cdk-py-pipeline",
      branch="main",
      connection_arn=connection_arn
    )
    
    base_commands = [
        "npm install -g aws-cdk",
        "pip install -r requirements.txt",
    ]

    # pipeline created to source from GitHub repo and synthesize a Cloud Assembly
    # from within the aws directory of the project
    pipeline = pipelines.CodePipeline(self, "Pipeline",
      synth=pipelines.ShellStep("Synth",
        input=source,
        commands=base_commands + [
          "npx cdk synth",
          "ls -l"
      ])
    )
    
    # infra_stage = InfrastructureStage(self, "Infra")
    # infra_deploy = pipeline.add_stage(infra_stage)
    # infra_deploy.add_pre(pipelines.ShellStep(
    #     "Test Infra",
    #     commands=base_commands + [
    #         "pip install -r requirements-dev.txt",
    #         "pytest"
    #     ]
    # ))
    # infra_deploy.add_post(pipelines.ShellStep(
    #     "Infra Post",
    #     commands=base_commands + [
    #         "ls -l"
    #     ]
    # ))

