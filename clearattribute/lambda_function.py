import json
import boto3

client = boto3.client('connect')

def lambda_handler(event, context):
    
    parameters = event['Details']['Parameters']['keep'].split(",")
    attributes = dict(event['Details']['ContactData']['Attributes'])
    contactID = str(event['Details']['ContactData']['ContactId'])
    newattrib = {}
    instanceID = event['Details']['ContactData']['InstanceARN'].split('/')[1]

    for key,value in attributes.items():
        if key in parameters:
            newattrib[key]=value
        else:
            newattrib[key]=''

    response = client.update_contact_attributes(
            InitialContactId = contactID,
            InstanceId = instanceID,
            Attributes=newattrib
        )

    return {
        'statusCode': 200,
    }

