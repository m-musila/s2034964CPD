# import packages
import sys
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

# load enviroment values for the ec2 instance.
load_dotenv() 
region = os.getenv("REGION_NAME")
keyId = os.getenv("AWS_ACCESS_KEY_ID")
key = os.getenv("AWS_SECRET_ACCESS_KEY")
token = os.getenv("AWS_SESSION_TOKEN")



# create ec2 resouce from boto3 with the enviroment variables
def ec2Instance():
    ec2 = boto3.resource("ec2",
                         region_name = region,
                         aws_access_key_id = keyId,
                         aws_secret_access_key = key,
                         aws_session_token = token
                         )
   # checks for return values and error conditions
    try:
        # create ec2 instance from above resource 
        instance = ec2.create_instances(
            # amazon machine image for this region and number of ec2 instances noted by min/max count
            ImageId="ami-006dcf34c09e50022",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="vockey"
        )
        print(instance)
    except ClientError as e:  
        print("ec2 instance error. Check implementation and try again!")

# Create the instance
ec2Instance()
        






























