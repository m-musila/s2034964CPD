import logging
import boto3
from botocore.exceptions import ClientError

# Create an S# bucket for the region
#If no region specified, the bucket is created in the S3 default us-east-1 region.
def create_bucket(bucket_name, region=None):
    # Create bucket and error handling
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    #return: True if bucket created, else False
    return True