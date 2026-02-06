# Github : https://github.com/Bllare
import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsTelketab(SmsProvider):
    name = "SMS Telketab"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
            data = f"identity={phone}&secret=&plugin=otp_field_sms_processor&key=otp_field_user_auth_form__otp_sms"

            response = requests.post("https://telketab.com/otp_field/check_secret" , data=data, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR