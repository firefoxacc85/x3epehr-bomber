from abc import ABC, abstractmethod
from apis.status import SendStatus

class CallProvider(ABC):
    name: str = "Base Call"

    @abstractmethod
    def call(self, phone: str) -> SendStatus:
        pass
