from typing import List

from fastapi import FastAPI

from app.database import initialize_db, users_table, categories_table, messages_table, default_users, default_categories
from app.schemas import UserModel, CategoryModel, MessageModel
from app.subscription.category import Category

app = FastAPI()
initialize_db()


@app.get("/users", response_model=List[UserModel])
def get_users():
    return users_table.all()

@app.get("/categories", response_model=List[CategoryModel])
def get_categories():
    return categories_table.all()

@app.get("/messages", response_model=List[MessageModel])
def get_messages():
    return messages_table.all()

@app.delete("/delete_all")
def delete_all():
    users_table.truncate()
    categories_table.truncate()
    messages_table.truncate()
    return {"message": "All tables has been deleted"}

@app.post("/default_data")
def default_data():
    users_table.insert_multiple(default_users)
    categories_table.insert_multiple(default_categories)
    return {"message": "Default data has been inserted"}

# @app.post("/send_message")
# def send_message(message: MessageModel):
#     messages_table.insert({"category": message.category, "message": message.message})
#     category = Category.from_string(message.category)
#     category.notify_subscribers(message.message)
#     return {"category": message.category, "message": message.message}
#
# #
# @app.post("/register_user")
# def register_user(user: UserModel):
#     users_table.insert(user.model_dump())
#     for category in user.categories:
#         category = Category.from_string(category)
#         category.add_subscriber(user.username)
#     return {"username": user.username, "category": user.categories}
