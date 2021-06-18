+++
title = "Completing the Pipeline"
weight = 70
+++

![](/30-pipeline/70-complete-pipeline-stage/pipeline_user_stages.png)

Let's complete the pipeline by adding the `Development` and `Production` stage.

Development stage can be added using the following lines in `pipeline_stack.py` 

```python
dev_stage = ApplicationDevStage(self, 'ApplicationDevStage', env=deployment_env)
pipeline_dev_stage = pipeline.add_application_stage(dev_stage)
```

Production stage can be added using the following lines in `pipeline_stack.py` 

```python
prod_stage = ApplicationProdStage(self, 'ApplicationProdStage', env=deployment_env)
pipeline.add_application_stage(prod_stage)
```

The pipeline is now complete. We now need to tell the CDK to deploy this pipeline.

