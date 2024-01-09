# AWS SageMaker DataSets CAT or DOG


### AWS CLI to invoke SageMaker Endpoint to predict if my image Cat or Dog:
```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name canvas-dog-cat      \
  --body fileb://YOURFILE.jpg         \
  --content-type=image/jpeg           \
  --accept "application/json" outfile.txt
```
