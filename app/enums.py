from enum import Enum


class TypeOfNotification(str, Enum):
    SMS = "SMS"
    EMAIL = "Email"
    PUSH_NOTIFICATION = "Push"


class Category(str, Enum):
    SPORTS = "Sports"
    FINANCE = "Finance"
    FILMS = "Films"
