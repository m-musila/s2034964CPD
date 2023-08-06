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

# create sns topic resouce from boto3 with the enviroment variables
def snsTopic():
    snsTopic = boto3.client("sns",
                              region_name = region,
                              aws_access_key_id = keyId,
                              aws_secret_access_key = key,
                              aws_session_token = token 
                              )
   # checks for return values and error conditions
    try:
        # create sqs topic url from above resource 
        topic = snsTopic.create_topic(Name="s2034964Topic")
        print("topic created")
    except ClientError as e:  
        print("sns topic instance error. Check implementation and try again!")

snsTopic()