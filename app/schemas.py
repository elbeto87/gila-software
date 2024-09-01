from typing import List

from pydantic import BaseModel

from app.subscription.enums import CategoryEnum, ChannelEnum


class MessageModel(BaseModel):
    category: CategoryEnum
    message: str


class UserModel(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    subscribed: List[CategoryEnum]
    channels: List[ChannelEnum]
