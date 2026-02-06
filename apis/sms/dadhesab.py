# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsDadhesab(SmsProvider):
    name = "SMS Dadhesab"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"username":phone,"deviceInfo":{"userAgent":headers["User-Agent"]},"appVersion":"10.4.5","appFlavor":"webapp"}

            response = requests.post("https://api.dadhesab.ir/user/login" , json=payload, headers=headers)
            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR