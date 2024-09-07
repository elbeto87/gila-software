from abc import abstractmethod

from app.subscription.enums import ChannelEnum
from app.logger import logger


class Notification:

    def __init__(self, type_of_notification: ChannelEnum):
        self.type_of_notification = type_of_notification

    @abstractmethod
    def send_message(self, user: str, message: str):
        raise NotImplementedError()

    @classmethod
    def from_str(cls, channel: str) -> 'Notification':
        match channel:
            case ChannelEnum.PUSH_NOTIFICATION:
                return PushNotification()
            case ChannelEnum.EMAIL:
                return EmailNotification()
            case ChannelEnum.SMS:
                return SMSNotification()
            case _:
                raise ValueError(f"Channel '{channel}' not found")


class PushNotification(Notification):

    def __init__(self):
        super().__init__(ChannelEnum.PUSH_NOTIFICATION)

    def send_message(self, user: str, message: str):
        logger.info(f"Sending PUSH notification to {user}: {message}")


class EmailNotification(Notification):

    def __init__(self):
        super().__init__(ChannelEnum.EMAIL)

    def send_message(self, user: str, message: str):
        logger.info(f"Sending Email to {user}: {message}")


class SMSNotification(Notification):

    def __init__(self):
        super().__init__(ChannelEnum.SMS)

    def send_message(self, user: str, message: str):
        logger.info(f"Sending SMS to {user}: {message}")
