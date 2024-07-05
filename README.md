# MLflow-Basic


## For Dagshub:

script.py:

```bash

import dagshub
import mlflow

dagshub.init(
  repo_owner='lequyan2003',
  repo_name='mlflow-practice',
  mlflow=True
)


with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)

```

# MLflow on AWS

## MLflow on AWS Setup:

1. Login to AWS console.
2. Create IAM user with AdministratorAccess
3. Export the credentials in your AWS CLI by running "aws configure"
4. Create a s3 bucket
5. Create EC2 machine (Ubuntu) & add Security groups 5000 port:
+ Security > Security groups > Edit inbound rules > Add rule > 5000 > 0.0.0.0/0

Run the following command on EC2 machine
```bash
sudo apt update

sudo apt install python3-pip

sudo apt install pipx

pipx ensurepath

pipx install pipenv

pipx install virtualenv

sudo apt install pipenv

sudo apt install virtualenv

# sudo pip3 install pipenv

# sudo pip3 install virtualenv

mkdir mlflow

cd mlflow

pipenv install mlflow

pipenv install awscli

pipenv install boto3

pipenv shell

## Then set aws credentials
aws configure

pip install setuptools

#Finally 
mlflow server -h 0.0.0.0 --default-artifact-root s3://mlflow-bucket-2003

#open Public IPv4 DNS to the port 5000


#set uri in your local terminal and in your code 
export MLFLOW_TRACKING_URI=http://ec2-3-88-235-207.compute-1.amazonaws.com:5000/ (unix shells only)
set MLFLOW_TRACKING_URI=http://ec2-3-88-235-207.compute-1.amazonaws.com:5000/ (Windows)
```
