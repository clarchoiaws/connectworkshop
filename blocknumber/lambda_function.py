def lambda_handler(event, context):

    CustomerNumber = event['Details']['ContactData']['CustomerEndpoint']['Address']

    print ('CustomerNumber is ', CustomerNumber)
    
    with open('block.txt') as datafile:
        if CustomerNumber in datafile.read():
            return {"block": "True"}
    return {"block": "False"}
