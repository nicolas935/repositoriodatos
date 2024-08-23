import boto3
client=client.boto3("s3","us-east-1")
response=client.list_buckets()
print(response)