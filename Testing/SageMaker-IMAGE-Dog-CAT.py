# ------------------------------------------------
# AWS SageMaker Invoke Endpoint by Denis Astahov
#
#
# Version      Date        Info
# 1.0          2024    Initial Version
#
# ------------------------------------------------
import boto3
import json
import os

AWS_ACCESS_KEY_ID = "xxxxxxxxxxxx"
AWS_SECRET_KEY_ID = "yyyyyyyyyyyyyyyyyyyyyyyyyyyy"
AWS_DEFAULT_REGION = "us-west-2"

IMAGE_FILENAME = "501.jpg"
ENDPOINT_NAME  = "canvas-dog-cat"

sagemaker = boto3.Session().client('sagemaker-runtime', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY_ID)
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

with open(IMAGE_FILENAME, 'rb') as f:
    payload = f.read()

response = sagemaker.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType='application/x-image', Body=payload, Accept="application/json")
result   = json.loads(response["Body"].read())
print(result)
print("Your Image: " + result["predicted_label"] + " is " + str(int(result["probability"] * 100)) + "%")

