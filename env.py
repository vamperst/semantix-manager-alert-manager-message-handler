import os

class Variables:
    def __init__(self):
        self.__arn_sns_alert_manager = os.environ.get('sns_alert_manager', '')

    def get_sns_alert_manager(self):
        return self.__arn_sns_alert_manager