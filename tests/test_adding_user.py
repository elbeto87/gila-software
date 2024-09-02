from http import HTTPStatus

from app.subscription.enums import CategoryEnum, ChannelEnum
from tests.conftest import client


class TestAddingUser:

    @classmethod
    def setup_class(cls):
        cls.client_data = {
            "id": 4,
            "name": "John Foo",
            "email": "john@foo.com",
            "phone": "1234567890",
            "subscribed": [CategoryEnum.SPORTS, CategoryEnum.FINANCE],
            "channels": [ChannelEnum.PUSH_NOTIFICATION],
            "messages_received": []
        }

    def test_adding_user(self, default_data):
        client.post("/create_user", json=self.client_data)

        assert client.get("/users").json()[-1] == self.client_data

    def test_remove_user(self, default_data):
        users = len(client.get("/users").json())
        response = client.delete("/delete_user/3")

        assert response.status_code == HTTPStatus.OK
        assert response.text == '{"message":"User has been deleted"}'
        assert len(client.get("/users").json()) == users - 1
