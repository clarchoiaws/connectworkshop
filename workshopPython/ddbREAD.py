import boto3
import json
from datetime import datetime

def lambda_handler(event, context):

    CallerID = event['Details']['Parameters']['CallerID']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CustomerTable')

    response = table.get_item(
            Key = { 'CallerID': CallerID }
        )

    if 'Item' in response:
        response['Item']['lambdaresults'] = 1
        return response['Item']
    else:
        return { "lambdaresults" : 0}
