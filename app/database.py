from tinydb import TinyDB

from app.subscription.enums import CategoryEnum, ChannelEnum

db = TinyDB('db.json')
users_table = db.table('users')
categories_table = db.table('categories')
messages_table = db.table('messages')


def initialize_db():

    if not users_table.all():
        users_table.insert_multiple(default_users)

    if not categories_table.all():
        categories_table.insert_multiple(default_categories)


default_users = [
    {
        "id": 681879266808159400,
        "name": "Grace",
        "email": "grace@example.com",
        "phone": "2223334444",
        "subscribed": [CategoryEnum.SPORTS, CategoryEnum.FINANCE],
        "channels": [ChannelEnum.EMAIL],
        "messages_received": []
    },
    {
        "id": 957748080764321000,
        "name": "Henry",
        "email": "henry@example.com",
        "phone": "5556667777",
        "subscribed": [CategoryEnum.FILMS],
        "channels": [ChannelEnum.PUSH_NOTIFICATION, ChannelEnum.SMS],
        "messages_received": []
    },
    {
        "id": -7570964647689087000,
        "name": "Isabella",
        "email": "isabella@example.com",
        "phone": "8889990000",
        "subscribed": [CategoryEnum.FILMS],
        "channels": [ChannelEnum.EMAIL],
        "messages_received": []
    },
]

default_categories = [
    {"name": CategoryEnum.SPORTS, "subscribers": [681879266808159400]},
    {"name": CategoryEnum.FILMS, "subscribers": [957748080764321000, -7570964647689087000]},
    {"name": CategoryEnum.FINANCE, "subscribers": [681879266808159400]},
]
