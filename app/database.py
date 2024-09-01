from tinydb import TinyDB

from app.subscription.enums import CategoryEnum, ChannelEnum

db = TinyDB('db.json')
users_table = db.table('users')
categories_table = db.table('categories')


def initialize_db():

    if not users_table.all():
        users_table.insert_multiple(default_users)

    if not categories_table.all():
        categories_table.insert_multiple(default_categories)

default_users = [
    {
        "id": 1,
        "name": "Grace",
        "email": "grace@example.com",
        "phone": "2223334444",
        "subscribed": [CategoryEnum.SPORTS, CategoryEnum.FINANCE],
        "channels": [ChannelEnum.EMAIL]
    },
    {
        "id": 2,
        "name": "Henry",
        "email": "henry@example.com",
        "phone": "5556667777",
        "subscribed": [CategoryEnum.FILMS],
        "channels": [ChannelEnum.PUSH_NOTIFICATION, ChannelEnum.SMS]
    },
    {
        "id": 3,
        "name": "Isabella",
        "email": "isabella@example.com",
        "phone": "8889990000",
        "subscribed": [CategoryEnum.FILMS],
        "channels": [ChannelEnum.EMAIL]
    },
]

default_categories = [
    {"name": CategoryEnum.SPORTS, "subscribers": []},
    {"name": CategoryEnum.FILMS, "subscribers": []},
    {"name": CategoryEnum.FINANCE, "subscribers": []},
]