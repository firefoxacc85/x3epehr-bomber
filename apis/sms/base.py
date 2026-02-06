# Github : https://github.com/Bllare

from abc import ABC, abstractmethod
from apis.status import SendStatus

class SmsProvider(ABC):
    name: str = "Base SMS"

    @abstractmethod
    def send(self, phone: str) -> SendStatus:
        pass
