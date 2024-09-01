from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.subscription.enums import CategoryEnum, ChannelEnum


class MessageModel(BaseModel):
    timestamp: datetime
    category: CategoryEnum
    message: str


class UserModel(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    subscribed: List[CategoryEnum]
    channels: List[ChannelEnum]


class CategoryModel(BaseModel):
    name: CategoryEnum
    subscribers: List[int]
