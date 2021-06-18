+++
title = "Source Action"
weight = 20
+++

![](/30-pipeline/20-source-actions/pipeline_source.png)

In this section, we will define a source.  

There are many possible options for a source like (S3, Codecommit, Github, Bitbucket, etc...)

#### CodeCommit source action
```python
source_action = cpactions.CodeCommitSourceAction(
            action_name="CodeCommit",
            output=source_artifact,
            repository="__ARN__OF__CODECOMMIT__REPO__",
        )
```
#### Github source action
```python
source_action = cpactions.GitHubSourceAction(
            action_name="Github",
            output=source_artifact,
            oauth_token=core.SecretValue.secrets_manager("cdk/githubtoken"),
            owner="ishan-aws",
            repo="cdk-pipelines-demo",
            trigger=cpactions.GitHubTrigger.POLL
        )
```

[Documentation of source actions](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-codepipeline-actions-readme.html#sources)


-----
-----

The `pipeline_stack.py` file should look like this
```python
class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        # Source
        source_action = cpactions.CodeCommitSourceAction(
            action_name="CodeCommit",
            output=source_artifact,
            repository="__ARN__OF__CODECOMMIT__REPO__",
        )
```
