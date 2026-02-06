# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsWatchonline(SmsProvider):
    name = "SMS Watchonline"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"mobile":phone}

            session = requests.Session()

            r = session.get("https://api.watchonline.shop/api/v1/init")
            
            token = r.json()["data"]["token"]
            headers["Authorization"] = f"Bearer {token}"

            response = session.post("https://api.watchonline.shop/api/v1/otp/request", json=payload, headers=headers)

            if response.status_code == 200 and response.json().get("code", 429) == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR