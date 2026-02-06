# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsSnapp(SmsProvider):
    name = "SMS Snapp"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            headers["Content-Type"] = "application/json"
            
            payload = {"cellphone":f"+98{int(phone)}","attestation":{"method":"skip","platform":"skip"},"extra_methods":[]}
            response = requests.post(f"https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp", json=payload, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 401:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR