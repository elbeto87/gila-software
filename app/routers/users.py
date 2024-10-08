from typing import List

from fastapi import APIRouter
from tinydb import Query

from app.database import users_table
from app.schemas import UserModel, UserCreationModel
from app.subscription.category import Category
from app.utils import is_id_duplicated, is_there_an_empty_field, add_suscribers_to_category

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[UserModel])
def get_users():
    return users_table.all()


@router.post("/", response_model=UserModel)
def create_user(user: UserCreationModel):
    user_id = str(hash(user.name))
    user_to_add = UserModel(
        id=user_id,
        name=user.name,
        email=user.email,
        phone=user.phone,
        subscribed=user.subscribed,
        channels=user.channels,
        messages_received=[]
    ).model_dump()
    is_id_duplicated(user_to_add["id"])
    is_there_an_empty_field(user_to_add)
    add_suscribers_to_category(user_to_add["subscribed"], user_to_add["id"])
    users_table.insert(user_to_add)

    return user_to_add


@router.delete("/{user_id}")
def delete_user(user_id: str):
    result = users_table.get(Query().id == user_id)
    users_table.remove(doc_ids=[result.doc_id])
    return {"message": "User has been deleted"}


@router.get("/{user_id}/messages_received", response_model=dict)
def get_messages_received(user_id: str):
    user = users_table.get(Query().id == user_id)
    return {"name": user["name"], "messages_received": user["messages_received"]}


@router.put("/{user_id}/subscribe_to_category/{category_name}")
def subscribe_to_category(user_id: str, category_name: str):
    user = users_table.get(Query().id == user_id)
    if category_name not in user["subscribed"]:
        Category.from_str(category_name).add_subscriber(user["id"])
        users_table.update({"subscribed": user["subscribed"]}, doc_ids=[user.doc_id])
    return {"message": f"User {user['name']} has been subscribed to category {category_name}"}
