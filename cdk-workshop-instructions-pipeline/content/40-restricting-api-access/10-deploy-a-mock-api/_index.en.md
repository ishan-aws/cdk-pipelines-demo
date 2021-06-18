+++
title = "Deploy our pipeline stack"
weight = 10
+++

We must now modify the `app.py` file to run the `PipelineStack`.

```python
app = core.App()

pl = PipelineStack(app, 'PipelineStack', env={
    "account": "__YOUR__ACCOUNT__ID__",
    "region": "ap-southeast-2"
})

app.synth()
```