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
        assert response.json() == {"message": "User has been deleted"}
        assert len(client.get("/users").json()) == users - 1

    def test_adding_same_user_id(self, default_data):
        client.post("/create_user", json=self.client_data)
        response = client.post("/create_user", json=self.client_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'detail': 'User ID already exists'}

    def test_adding_with_empty_field(self, default_data):
        field_to_test = "name"
        self.client_data[field_to_test] = ""
        response = client.post("/create_user", json=self.client_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {"detail": f"Field {field_to_test} is empty"}
