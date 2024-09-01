from app.main import logger


class Subscriber:

    def __init__(self, name: str, type_of_notification: list[str]):
        self.name = name
        self.type_of_notification = type_of_notification

    def update(self, message):
        logger.info(f"Sending message to {self.name}: {message}")
        for notification in self.type_of_notification:
            notification.send_message(message)
