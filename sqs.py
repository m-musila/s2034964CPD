# import packages
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

# load enviroment values for the sqs queue.
load_dotenv() 
region = os.getenv("region_name")
keyId = os.getenv("aws_access_key_id")
key = os.getenv("aws_secret_access_key")
token = os.getenv("aws_session_token")

# create sqs queue resouce from boto3 with the enviroment variables
def sqsQueue():
    sqsQueue = boto3.resource("sqs",
                              region_name = region,
                              aws_access_key_id = keyId,
                              aws_secret_access_key = key,
                              aws_session_token = token 
                              )
   # checks for return values and error conditions
    try:
        # create sqs queue instance from above resource 
        queue = sqsQueue.create_queue(queueName="s2034964Queue")
        print(queue.url)
    except ClientError as e:  
        print("sqs queue instance error. Check implementation and try again!")

