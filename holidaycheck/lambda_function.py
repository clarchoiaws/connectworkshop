import datetime
import dateutil.tz

def lambda_handler(event, context):

    # Timezone default to US/Eastern if it is not passed in through Parameters
    
    param = event['Details']['Parameters']

    if "timezone" in param:
        timezone = param['timezone']
    else:
        timezone = 'US/Eastern'

    eastern = dateutil.tz.gettz(timezone)

    d1 = datetime.datetime.now(tz=eastern) 
    
    today = str(d1.date())
    print ('today is ', today)
    with open('holidays.txt') as datafile:
        if today in datafile.read():
            return {"holiday": "True"}
    return {"holiday": "False"}