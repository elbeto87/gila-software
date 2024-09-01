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

@app.get("/users/{user_id}/messages_received", response_model=dict)
def get_messages_received(user_id: int):
    user = users_table.get(doc_id=user_id)
    return {"name": user["name"], "messages_received": user["messages_received"]}

@app.post("/send_message")
def send_message(message: MessageModel):
    messages_table.insert(message.model_dump())
    category = Category.from_string(message.category)
    category.notify_subscribers(message)

@app.post("/default_data")
def default_data():
    users_table.truncate()
    categories_table.truncate()
    messages_table.truncate()
    users_table.insert_multiple(default_users)
    categories_table.insert_multiple(default_categories)
    return {"message": "Default data has been inserted"}


# ID should be the hash of the name (change default_users)
# Register new User
# Register new Category
# Register new Channel
# Tests
# Dockerize
