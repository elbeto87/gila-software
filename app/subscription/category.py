class Category:

    def __init__(self, name: str):
        self.name = name
        self.subscribers = []

    def __str__(self):
        return self.name

    @classmethod
    def from_string(cls, category: str):
        return cls(category)

    def add_subscriber(self, username: str):
        self.subscribers.append(username)

    def notify_subscribers(self, message: str):
        for subscriber in self.subscribers:
            print(f"Sending message to {subscriber} in category {self.name}: {message}")
            subscriber.update(message)
