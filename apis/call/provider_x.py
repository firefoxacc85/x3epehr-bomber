import time
from apis.call.base import CallProvider
from apis.status import SendStatus

class CallProviderX(CallProvider):
    name = "CALL Provider X"

    def call(self, phone: str) -> SendStatus:
        time.sleep(0.5)
        return SendStatus.SENT
