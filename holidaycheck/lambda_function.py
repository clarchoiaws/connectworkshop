import datetime
import dateutil.tz

def lambda_handler(event, context):

    eastern = dateutil.tz.gettz('US/Eastern')

    d1 = datetime.datetime.now(tz=eastern) 
    
    today = str(d1.date())
    print (today)
    with open('holidays.txt') as datafile:
        if today in datafile.read():
            return {"holiday": "True"}
    return {"holiday": "False"}
