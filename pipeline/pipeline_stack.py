from aws_cdk import core, aws_codepipeline as codepipeline, aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
from aws_cdk import aws_codecommit as codecommit

from .pipeline_stages import ApplicationDevStage, ApplicationProdStage


class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        # Source
        repo = codecommit.Repository.from_repository_name(self, "CodeRepo", repository_name="cdkworkshop")
        source_action = cpactions.CodeCommitSourceAction(
            action_name="CodeCommit",
            output=source_artifact,
            repository=repo,
            branch="master"
        )

        # Synthesise
        synth_action = pipelines.SimpleSynthAction(
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_assembly_artifact,
            install_command="npm install -g aws-cdk && pip install -r requirements.txt",
            synth_command="cdk synth"
        )

        # The pipeline
        pipeline = pipelines.CdkPipeline(self, "Pipeline",
                                         cloud_assembly_artifact=cloud_assembly_artifact,
                                         pipeline_name="ServerlessPipeline",
                                         source_action=source_action,
                                         synth_action=synth_action)

        pipeline.add_application_stage(ApplicationDevStage(self, 'ApplicationDevStage'))
        pipeline.add_application_stage(ApplicationProdStage(self, 'ApplicationProdStage'), manual_approvals=True)
