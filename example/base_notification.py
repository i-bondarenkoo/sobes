from abc import ABC, abstractmethod


class BaseNotification(ABC):
    def __init__(
        self,
        notify_type: str,
    ):
        self.notify_type = notify_type

    @abstractmethod
    def send_notify(self):
        pass
