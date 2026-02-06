# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsSnappDigital(SmsProvider):
    name = "SMS Snapp Digital"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"cellphone": phone}

            response = requests.post("https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp" , json=payload, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR