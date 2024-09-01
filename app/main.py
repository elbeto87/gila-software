from typing import List

from fastapi import FastAPI

from app.database import initialize_db, users_table, categories_table
from app.schemas import UserModel

app = FastAPI()
initialize_db()


@app.get("/users", response_model=List[UserModel])
def get_users():
    return users_table.all()

@app.get("/categories")
def get_categories():
    return categories_table.all()


# @app.post("/send_message")
# def send_message(message: MessageModel):
#     messages.append({"category": message.category, "message": message.message})
#     category = Category.from_string(message.category)
#     category.notify_subscribers(message.message)
#     return {"category": message.category, "message": message.message}

#
# @app.post("/register_user")
# def register_user(user: UserRegistrationModel):
#     users.append({"username": user.username, "category": user.categories})
#     for category in user.categories:
#         category = Category.from_string(category)
#         category.add_subscriber(user.username)
#     return {"username": user.username, "category": user.categories}
