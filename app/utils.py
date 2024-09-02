from fastapi import HTTPException
from tinydb import Query

from app.database import users_table


def is_id_duplicated(user_id: int):
    if users_table.search(Query().id == user_id):
        raise HTTPException(status_code=400, detail="User ID already exists")


def is_there_an_empty_field(user_to_add: dict):
    for key, value in user_to_add.items():
        if key == "messages_received":
            continue
        if not value:
            raise HTTPException(status_code=400, detail=f"Field {key} is empty")


def is_category_name_duplicated(category_name: str):
    if users_table.search(Query().name == category_name):
        raise HTTPException(status_code=400, detail="Category name already exists")