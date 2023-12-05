import boto3
def get_
instance_name (instance_id, ec2_client):
response
ec2_client describe_instances(Instancelds=[instance_id])
reservations = response['Reservations']
for reservation in reservations:
for instance in reservation Instances']:
return instance.getTags', [f'Key': 'Name', "Value': "N/A'}1)[010'Value']
def
get_eips_and_associated_resources ():
ec2_client = boto3. client (ec2')
# Describe
all
Elastic IPs
eip_response = ec2_client. describe_addresses ()
for eip in eip_responsel Addresses']:
print(f"Elastic IP: {eip['PublicIp']}")
# Check if there
are
associated instances
if "InstanceId"
in eip:
instance_id = eipt Instanceld']
instance_name = get_instance_name (instance_id,
ec2_client)
print(f"
Associated Instance ID: (instance_id)")
print (f"
Associated Instance Name: {instance_name?")
print ("")
# Call
the function
get_eips_and_associated_resources)
