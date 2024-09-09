from typing import List

from fastapi import APIRouter

from app.database import messages_table
from app.schemas import MessageModel
from app.subscription.category import Category
from app.utils import is_there_an_empty_field


router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[MessageModel])
def get_messages():
    return messages_table.all()


@router.post("/")
def send_message(message: MessageModel):
    message_to_send = message.model_dump()
    is_there_an_empty_field(message_to_send)
    messages_table.insert(message_to_send)
    category = Category.from_str(message_to_send["category"])
    category.notify_subscribers(message_to_send)
    return message
