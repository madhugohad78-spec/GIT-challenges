echo "import boto3

# Create EC2 client
ec2 = boto3.resource(
    'ec2',
    region_name='ap-south-1'
)

# Create EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0f58b397bc5c1f2e8',  # Example Amazon Linux AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair-name',
    SecurityGroupIds=['sg-xxxxxxxx'],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Python-EC2'
                }
            ]
        }
    ]
)

instance = instances[0]

print("Launching instance...")

# Wait until running
instance.wait_until_running()

instance.reload()

print("EC2 Instance Created")
print("Instance ID:", instance.id)
print("Public IP:", instance.public_ip_address)" > app.py
