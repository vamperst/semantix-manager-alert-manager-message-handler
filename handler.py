import json
from snsHandler import SnsHandler


def messagehandler(event, context):
    dictJson = json.loads(event['body'])

    print(dictJson['alerts'][0])
    baseDict = {'startat': str(dictJson['alerts'][0]['startsAt']),'severity':str(dictJson['alerts'][0]['labels']['severity']),'description':str(dictJson['alerts'][0]['annotations']['description'])}
    base = "Alarm started at: {startat}\nSeverity: {severity}\nDescription: {description}"
    base = base.format(startat=baseDict['startat'], severity=baseDict['severity'],description=baseDict['description'])
    print(base)
    sns = SnsHandler()
    sns.publishToSnsAlertManager('Semantix Manager alert ' + baseDict['severity'],base)
    
    
    body = {
        "message":json.dumps(dictJson)
    }


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response