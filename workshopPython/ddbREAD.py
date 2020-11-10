import boto3
import json
from datetime import datetime

def lambda_handler(event, context):

    CallerID = event['Details']['Parameters']['CallerID']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('AmazonConnectLab1001Table')

    response = table.get_item(
            Key = { 'CallerID': CallerID }
        )

    if 'Item' in response:
        response['Item']['recordFound'] = "True"
        response['Item']['lambdaResult'] = "Success"
        return response['Item']
    else:
        return { "lambdaResult" : "Error"}
