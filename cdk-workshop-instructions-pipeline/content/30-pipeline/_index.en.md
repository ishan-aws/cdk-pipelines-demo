+++
title = "Defining the Pipeline"
chapter = true
weight = 30
pre = "<b>3. </b>"
+++

In this part of the exercise we are going to define a pipeline using the CDK. 

The goal will be to have the pipeline synthesize and deploy our stacks automatically. 

This is best practice when CI/CD processes. With the new CDK Pipelines, you can version control your pipeline. 

The pipeline will update itself first and then deploy the code each time a change is detected in source control. 
Self mutation is prebuilt by the CDK team and comes with the `aws_cdk` package. 

A stage is a logical unit that can isolate an environment and limit the number of concurrent changes. 

Each pipeline must have at least two stages;
* Source
* Any other stage that is not source

In our case, we have 5 stages. 
* Source
* Update Pipeline
* Build
* Development Deployment
* Production Deployment (requires manual approval)

![](/30-pipeline/pipeline_base.png)