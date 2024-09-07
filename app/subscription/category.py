from app.database import categories_table
from app.logger import logger
from app.subscription.enums import CategoryEnum
from app.subscription.subscriber import Subscriber


class Category:

    def __init__(self, name: CategoryEnum, subscribers: list):
        self.name = name
        self.subscribers = subscribers

    def __str__(self):
        return self.name

    @classmethod
    def from_string(cls, category: str) -> 'Category':
        categories = categories_table.all()
        category_found = next((c for c in categories if c['name'] == category), None)
        if not category_found:
            raise ValueError(f"Category '{category}' not found")
        return cls(**category_found)

    def add_subscriber(self, username: str):
        logger.info(f"Adding {username} to category {self.name}")
        self.subscribers.append(username)

    def notify_subscribers(self, message: dict):
        for subscriber in self.subscribers:
            subscriber = Subscriber.from_int(subscriber)
            logger.info(f"Sending message to '{subscriber.name}' in category '{self.name}'")
            subscriber.update(message=message)
