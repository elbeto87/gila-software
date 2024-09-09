from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from app.subscription.enums import CategoryEnum, ChannelEnum


class MessageModel(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    category: CategoryEnum
    message: str

    def model_dump(self, *args, **kwargs):
        return {
            "timestamp": self.timestamp.isoformat(),
            "category": self.category.value,
            "message": self.message,
        }


class UserModel(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    subscribed: List[CategoryEnum]
    channels: List[ChannelEnum]
    messages_received: List[dict]


class UserCreationModel(BaseModel):
    name: str = "John Doe"
    email: str = "john_doe@gmail.com"
    phone: str = "111-222-3333"
    subscribed: List[CategoryEnum] = [CategoryEnum.FILMS, CategoryEnum.FINANCE]
    channels: List[ChannelEnum] = [ChannelEnum.EMAIL]


class CategoryModel(BaseModel):
    name: CategoryEnum
    subscribers: List[str]
