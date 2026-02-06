# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsDigify(SmsProvider):
    name = "SMS Digify"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            headers["Content-Type"] = "application/json"
            payload = {"phone_number": phone}

            response = requests.post("https://backend.digify.shop/user/merchant/otp/" , json=payload, headers=headers)
            if response.status_code == 201:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR