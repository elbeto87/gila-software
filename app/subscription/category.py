from app.enums import CategoryEnum
from app.main import logger


class Category:

    def __init__(self, name: CategoryEnum):
        self.name = name
        self.subscribers = []

    def __str__(self):
        return self.name

    @classmethod
    def from_string(cls, category: CategoryEnum):
        return cls(category.value)

    def add_subscriber(self, username: str):
        logger.info(f"Adding {username} to category {self.name}")
        self.subscribers.append(username)

    def notify_subscribers(self, message: str):
        logger.info(f"Sending message to {self.subscribers} in category {self.name}: {message}")
        for subscriber in self.subscribers:
            logger.info(f"Sending message to {subscriber} in category {self.name}")
            subscriber.update(message)
