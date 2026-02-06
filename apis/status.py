from enum import Enum, auto

class SendStatus(Enum):
    SENT = auto()
    FAILED = auto()
    ERROR = auto()
    UNKNOWN = auto()
