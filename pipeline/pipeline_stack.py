from aws_cdk import core, aws_codepipeline as codepipeline, aws_codepipeline_actions as cpactions
from aws_cdk import pipelines

from .serverless_stage import ServerlessStage

APP_ACCOUNT = "##CHANGE##"


class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        source_action = cpactions.GitHubSourceAction(
            action_name="Github",
            output=source_artifact,
            oauth_token=core.SecretValue.secrets_manager("cdk/githubtoken"),
            owner="ishan-aws",
            repo="cdk-pipelines-demo",
            trigger=cpactions.GitHubTrigger.POLL
        )
        synth_action = pipelines.SimpleSynthAction(
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_assembly_artifact,
            install_command="npm install -g aws-cdk && pip install -r requirements.txt",
            synth_command="cdk synth"
        )

        pipeline = pipelines.CdkPipeline(self, "Pipeline",
                                         cloud_assembly_artifact=cloud_assembly_artifact,
                                         pipeline_name="ServerlessPipeline",
                                         source_action=source_action,
                                         synth_action=synth_action)

        stage = ServerlessStage(self, 'TestDeploy', env={
            "account": "555618984259",
            "region": "us-east-1"
        })

        pipeline.add_application_stage(stage)
