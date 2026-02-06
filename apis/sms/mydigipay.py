# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsMydigipay(SmsProvider):
    name = "SMS Mydigipay"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"cellNumber": phone,"device": {"deviceId": "a16e6255-17c3-431b-b047-3f66d24c286f","deviceModel": "WEB_BROWSER","deviceAPI": "WEB_BROWSER","osName": "WEB"}}

            response = requests.post("https://app.mydigipay.com/digipay/api/users/send-sms" , json=payload, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR