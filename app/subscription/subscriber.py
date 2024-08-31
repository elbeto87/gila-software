from app.main import logger


class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        logger.info(f"Sending message to {self.name}: {message}")
