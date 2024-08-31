from fastapi import FastAPI

from app.enums import CategoryEnum
from app.logger import logger
from app.subscription.category import Category
from .models import MessageModel, UserRegistrationModel

app = FastAPI()

users = []
messages = []

sports_category = Category(CategoryEnum.SPORTS)
finance_category = Category(CategoryEnum.FINANCE)
films_category = Category(CategoryEnum.FILMS)


@app.get("/users")
def get_users():
    logger.info(f"Getting users: {users}")
    return {"users": users}


@app.post("/send_message")
def send_message(message: MessageModel):
    messages.append({"category": message.category, "message": message.message})
    category = Category.from_string(message.category)
    category.notify_subscribers(message.message)
    return {"category": message.category, "message": message.message}


@app.post("/register_user")
def register_user(user: UserRegistrationModel):
    users.append({"username": user.username, "category": user.categories})
    for category in user.categories:
        category = Category.from_string(category)
        category.add_subscriber(user.username)
    return {"username": user.username, "category": user.categories}
