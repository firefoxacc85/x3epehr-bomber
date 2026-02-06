import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

NUMBERS_FILE = DATA_DIR / "numbers.json"
SETTINGS_FILE = DATA_DIR / "settings.json"


class Storage:
    @staticmethod
    def load_numbers() -> dict:
        if not NUMBERS_FILE.exists():
            return {}
        return json.loads(NUMBERS_FILE.read_text(encoding="utf-8"))

    @staticmethod
    def save_numbers(data: dict):
        NUMBERS_FILE.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    @staticmethod
    def load_settings() -> dict:
        if not SETTINGS_FILE.exists():
            return {
                "sms_delay": 1.5,
                "loop_delay": 60,
                "enable_sms": True,
                "enable_call": False,
            }
        return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))

    @staticmethod
    def save_settings(data: dict):
        SETTINGS_FILE.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
