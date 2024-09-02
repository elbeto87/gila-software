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


    def test_sending_message_with_invalid_category(self, default_data):
        message_data = self.message_data.copy()
        message_data["category"] = "Invalid Category"
        response = client.post("/send_message", json=message_data)

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Input should be 'Sports', 'Finance', 'Films' or 'Education'"

    def test_sending_message_without_message(self, default_data):
        message_data = self.message_data.copy()
        message_data["message"] = ""
        response = client.post("/send_message", json=message_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {"detail": "Field message is empty"}

    def test_message_is_received(self, default_data):
        client.post("/send_message", json=self.message_data)
        response = client.get("/users/2/messages_received")

        assert response.status_code == HTTPStatus.OK
        assert any(msg["message"] == self.message_data["message"] for msg in response.json()["messages_received"])
