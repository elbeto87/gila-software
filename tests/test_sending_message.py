from http import HTTPStatus

from app.subscription.enums import CategoryEnum
from tests.conftest import client


class TestSendingMessage:

    @classmethod
    def setup_class(cls):
        cls.message_data = {
            "timestamp": "2021-01-01T12:00:00",
            "category": CategoryEnum.FILMS,
            "message": "New film is Godfather",
        }


    def test_sending_message(self, default_data):
        response = client.post("/send_message", json=self.message_data)

        assert response.status_code == HTTPStatus.OK
        assert client.get("/messages").json()[-1] == self.message_data
