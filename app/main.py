import logging

from fastapi import FastAPI

from app.subscription.category import Category
from .models import MessageModel, UserRegistrationModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

users = []
messages = []


@app.get("/users")
def get_users():
    logger.info(f"Users: {users}")
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
