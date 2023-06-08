import boto3
from botocore.exceptions import ClientError



port = 22
#List all the security groups
#check each SG wih public inbount 22
#Update the SG with 10.0.0.0/8,192.172
all_sgid = list()

#Fetching all the SGs
ec2 = boto3.client('ec2', region_name='us-west-2')
sgs = ec2.describe_security_groups()
sg = sgs['SecurityGroups']

'''
#Fetching the sgid
for gid in sg:
    all_sgid.append(gid['GroupId'])

#working listing sgid
for i in all_sgid:
    print (i)
'''


for gid in sg:
    for i in range(len(gid['IpPermissions'])):
        for j in range(len(gid['IpPermissions'][i]['IpRanges'])):
            if "0.0.0.0/0" in gid['IpPermissions'][i]['IpRanges'][j]['CidrIp'] and port == gid['IpPermissions'][i]['FromPort']:
                print (gid['GroupId'])
                print (gid['IpPermissions'][i]['FromPort'])
                print (gid['IpPermissions'][i]['IpRanges'][j]['CidrIp'])
