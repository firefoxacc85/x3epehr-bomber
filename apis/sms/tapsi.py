# Github : https://github.com/Bllare
import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsTapsi(SmsProvider):
    name = "SMS Tapsi"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            payload = {"credential": {"phoneNumber": phone, "role": "DRIVER"}, "otpOption": "SMS"}

            response = requests.post("https://api.tapsi.ir/api/v2.2/user" , json=payload, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR