# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsNeshan(SmsProvider):
    name = "SMS Neshan"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            uid  = uuid.uuid1()
            
            response = requests.get(f"https://neshan.org/maps/pwa-api/login/sms/request?mobileNumber={phone}&uuid=web_{uid}", headers=headers)
            
            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR