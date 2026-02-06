# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsAdinehbook(SmsProvider):
    name = "SMS Adinehbook"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            data = f"path=&action=sign&phone_cell_or_email={phone}&login-submit=%D8%AA%D8%A7%DB%8C%DB%8C%D8%AF"

            response = requests.post("https://www.adinehbook.com/gp/flex/sign-in.html" , data=data, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR