class Subscriber:

    def __init__(self, user_id, name, email, phone, subscribed, channels):
        self.id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.subscribed = subscribed
        self.channels = channels

    @classmethod
    def from_int(cls, subscriber: int):
        return cls(**users_table.get(doc_id=subscriber))

    def update(self, message):
        for notification in self.type_of_notification:
            notification.send_message(message)
