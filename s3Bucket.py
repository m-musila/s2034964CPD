import time
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv


# load enviroment values for the sqs queue.
load_dotenv() 
region = os.getenv("REGION_NAME")
keyId = os.getenv("AWS_ACCESS_KEY_ID")
key = os.getenv("AWS_SECRET_ACCESS_KEY")
token = os.getenv("AWS_SESSION_TOKEN")


# The bucket is created in the S3 default us-east-1 region. the image uplaod done
def s3BucketAndFileUpload(image, objectName):
    # Create an S3 bucket for the region 
    client = boto3.resource("s3",
                              region_name = region,
                              aws_access_key_id = keyId,
                              aws_secret_access_key = key,
                              aws_session_token = token 
                              )
    # Access image location
    imageLocation = os.getcwd()
    # My image bucket
    bucketName = "s2034964ImgS3Bucket"
    # Access image name using images folder dir
    imageName = os.path.join(imageLocation, "images", image)

    # checks for return values and error conditions
    try:
        # upload images to s3 bucket
        client.upload_file(objectName, bucketName, imageName)
        print("Upload was successful")
    except ClientError as e:  
        print("could not upload file")

# upload file with 30 seconds intervals. 
for i in range(1,6):

    #Running loop from 1 to 6
    image = "image" + str(i) + ".jpg"
    object = "object" + str(i) + ".jpg" 
    s3BucketAndFileUpload(image, object)

    # adding 30 seconds time delay
    time.sleep(30)
