from app.database import users_table
from app.logger import logger
from app.schemas import MessageModel


class Subscriber:

    def __init__(self, id, name, email, phone, subscribed, channels, messages_received):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.subscribed = subscribed
        self.channels = channels
        self.message_received = messages_received

    @classmethod
    def from_int(cls, subscriber: int) -> 'Subscriber':
        users = users_table.all()
        user_found = next((u for u in users if u["id"] == subscriber), None)
        if not user_found:
            raise ValueError(f"User '{user_found}' not found")
        return cls(**user_found)

    def update(self, message: MessageModel):
        for channel in self.channels:
            logger.info(f"Using channel '{channel}': {message}")
            self.message_received.append(
                {
                    "channel": channel,
                    "message": message.model_dump()
                }
            )
            users_table.update({"messages_received": self.message_received}, doc_ids=[self.id])
