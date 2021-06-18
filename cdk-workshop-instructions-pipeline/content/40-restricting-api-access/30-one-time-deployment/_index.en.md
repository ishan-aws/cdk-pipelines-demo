+++
title = "Push your code"
weight = 20
+++

Only once, you'll need to run deploy from the terminal. 

Once the pipeline is deployed once manually, it is self-mutating.

Please run the following commands
```python
cdk bootstrap
cdk synth # check if it works
cdk deploy
```

You will not have to run this again. 