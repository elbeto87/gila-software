from tinydb import Query

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
    def from_str(cls, category: str) -> 'Category':
        categories = categories_table.all()
        category_found = next((c for c in categories if c['name'] == category), None)
        if not category_found:
            raise ValueError(f"Category '{category}' not found")
        return cls(**category_found)

    def add_subscriber(self, user_id: int):
        logger.info(f"Adding user_id #'{user_id}' to category {self.name}")
        categories_table.update({"subscribers": self.subscribers + [user_id]}, Query().name == self.name)

    def notify_subscribers(self, message: dict):
        for subscriber in self.subscribers:
            subscriber = Subscriber.from_int(subscriber)
            subscriber.update(message=message)
