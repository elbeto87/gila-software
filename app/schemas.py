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
    id: int
    name: str
    email: str
    phone: str
    subscribed: List[CategoryEnum]
    channels: List[ChannelEnum]
    messages_received: List[dict]


class CategoryModel(BaseModel):
    name: CategoryEnum
    subscribers: List[int]
