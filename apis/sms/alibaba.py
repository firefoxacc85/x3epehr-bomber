# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsAlibaba(SmsProvider):
    name = "SMS Alibaba"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"phoneNumber": phone}

            response = requests.post(f"https://ws.alibaba.ir/api/v3/account/mobile/otp", headers=headers,json=payload)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR