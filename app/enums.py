from enum import Enum


class TypeOfNotification(str, Enum):
    SMS = "sms"
    EMAIL = "email"
    PUSH_NOTIFICATION = "push"


class Category(str, Enum):
    SPORTS = "sports"
    FINANCE = "finance"
    FILMS = "films"
