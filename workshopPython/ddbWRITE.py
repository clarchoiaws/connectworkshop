import boto3
import json
from datetime import datetime
import random

def lambda_handler(event, context):

    CallerID = event['Details']['ContactData']['CustomerEndpoint']['Address']
    CallerPIN = random.randint(1111,9999)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CustomerTable')

    try:
        response = table.put_item(
            Item = { 
                'CallerID': CallerID,
                'callerPIN': CallerPIN,
                'firstName': 'New',
                'lastName': 'Customer',
                'custLevel': 'Welcome',
                'language': event['Details']['Parameters']['language']
            },
            ConditionExpression = 'CallerID <> :cid',
            ExpressionAttributeValues = {':cid':CallerID}
        )
        result = 200
    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException as e:
        print('error is ',e)
        result = 500

    if result == 200:
        client = boto3.client('sns')
        snsresponse = client.publish(
                PhoneNumber=CallerID,
                Message="Thank you for signing up.  Your PIN is " + str(CallerPIN)
            )

    return {
        'statusCode': result,
        'CallerPIN': CallerPIN
    }
