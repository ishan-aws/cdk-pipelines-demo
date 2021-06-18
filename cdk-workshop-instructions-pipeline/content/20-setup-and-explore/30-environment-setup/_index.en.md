+++
title = "Environment Setup"
chapter = false
weight = 23
+++




#### Virtual Environment
We shall now create and activate a Python virtual environment.

Navigate to the project directory

```shell
cd cdk-pipelines-demo
```

Now create and activate the virtual environment
```shell
python -m venv .env
source .env/bin/activate
```

-----
-----

#### Dependencies
Installing the dependencies
```shell
pip install -r requirements.txt
```
This will go ahead and now install the Python `aws_cdk` dependencies for services like Lambda, ApiGateway, Pipeline the lab needs. 

> Note: If you `pip install` other libraries, add them to requirements.txt. A helpful command is `pip freeze > requirements.txt`

