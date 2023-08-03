import boto3

# ec2 resouce form boto3 
ec2 = boto3.resource("ec2")

# create ec2 instance 
instance = ec2.create_instances(
    # amazon machine image for this region and number of ec2 instances noted by min/max xount
    ImageId="ami-0dafa01c8100180f8",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="KeyPair1"
)
