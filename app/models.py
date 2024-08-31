from pydantic import BaseModel

from .enums import Category


class MessageModel(BaseModel):
    category: Category
    message: str


class UserRegistrationModel(BaseModel):
    username: str
    categories: list[Category]
    messages: list[MessageModel] = []
