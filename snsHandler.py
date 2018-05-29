import json
import boto3
from env import Variables

class SnsHandler:
    def __init__(self):
        self.__sns = boto3.client('sns')
        self.env = Variables()
    
    def __publishToSns(self,subject,message,arn):
        response = self.__sns.publish(
            TopicArn=self.env.get_sns_alert_manager(),
            Message=message,
            Subject=subject
        )
        print(str(response))

    def publishToSnsAlertManager(self,subject,message):
        return self.__publishToSns(subject,message,self.env.get_sns_alert_manager())
    
        
    
        