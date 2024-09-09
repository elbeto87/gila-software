from app.subscription.enums import CategoryEnum, ChannelEnum

category_data = {
    "name": CategoryEnum.EDUCATION,
    "subscribers": []
}

message_data = {
    "timestamp": "2021-01-01T12:00:00",
    "category": CategoryEnum.FILMS,
    "message": "New film is Godfather",
}

message_education_data = {
    "timestamp": "2021-01-01T12:00:00",
    "category": CategoryEnum.EDUCATION,
    "message": "College is important",
}

client_data = {
    "name": "John Foo",
    "email": "john@foo.com",
    "phone": "1234567890",
    "subscribed": [CategoryEnum.SPORTS, CategoryEnum.FINANCE],
    "channels": [ChannelEnum.PUSH_NOTIFICATION],
}

client_data_with_education = {
    "name": "John Foo",
    "email": "john@foo.com",
    "phone": "1234567890",
    "subscribed": [CategoryEnum.EDUCATION],
    "channels": [ChannelEnum.PUSH_NOTIFICATION],
}