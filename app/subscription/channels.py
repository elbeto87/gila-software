from app.subscription.enums import ChannelEnum
from app.logger import logger


class Notification:

    def __init__(self, type_of_notification: ChannelEnum):
        self.type_of_notification = type_of_notification

    def send_message(self, user: str, message: str):
        logger.info(f"Sending {self.type_of_notification} message '{message}' to user: {user}")
