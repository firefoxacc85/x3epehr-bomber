# Github : https://github.com/Bllare
import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsDrnext(SmsProvider):
    name = "SMS Drnext"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"source": "besina","mobile": phone}

            response = requests.post("https://cyclops.drnext.ir/v1/patients/auth/send-verification-token" , json=payload, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR