from PySide6.QtCore import QRunnable, QObject, Signal, Slot
import requests


class WorkerSignals(QObject):
    result = Signal(object)
    log = Signal(str)


class SendWorker(QRunnable):
    def __init__(self, api, phone, stop_event):
        super().__init__()
        self.api = api
        self.phone = phone
        self.stop_event = stop_event
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        # ✅ exit immediately if stop requested
        if self.stop_event.is_set():
            return

        try:
            result = self.api.send(self.phone)

            if self.stop_event.is_set():
                return

            status = result[0] if isinstance(result, tuple) else result
            self.signals.result.emit(status)

            status_name = getattr(status, "name", str(status))
            self.signals.log.emit(f"{self.api.name} -> {status_name}")

        except requests.exceptions.Timeout:
            self.signals.log.emit(f"{self.api.name} -> TIMEOUT")

        except Exception:
            self.signals.log.emit(f"{self.api.name} -> ERROR")
