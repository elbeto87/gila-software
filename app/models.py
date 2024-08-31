from pydantic import BaseModel

from app.enums import Category


class UserRegistration(BaseModel):
    username: str
    categories: list[Category]
