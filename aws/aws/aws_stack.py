from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines
)


class PipelineStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, connection_arn: str, **kwargs):
    super().__init__(scope, construct_id, **kwargs)
    
    # source code location referenced via GitHub Connection
    source = pipelines.CodePipelineSource.connection(
      repo_string="amcquistan/cdk-py-pipeline",
      branch="main",
      connection_arn=connection_arn
    )
    
    # pipeline created to source from GitHub repo and synthesize a Cloud Assembly
    # from within the aws directory of the project
    pipeline = pipelines.CodePipeline(self, "Pipeline",
      synth=pipelines.ShellStep("Synth",
        input=source,
        primary_output_directory="aws/cdk.out",
        commands=[
          "cd aws",
          "npm install -g aws-cdk",
          "pip install -r requirements.txt",
          "npx cdk synth"
      ])
    )



