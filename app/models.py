from pydantic import BaseModel

from .enums import CategoryEnum


class MessageModel(BaseModel):
    category: CategoryEnum
    message: str


class UserRegistrationModel(BaseModel):
    username: str
    categories: list[CategoryEnum]
    messages: list[MessageModel] = []
