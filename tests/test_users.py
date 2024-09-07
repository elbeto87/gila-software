from http import HTTPStatus

from app.subscription.enums import CategoryEnum, ChannelEnum
from tests.conftest import client


class TestUsers:

    @classmethod
    def setup_class(cls):
        cls.client_data = {
            "name": "John Foo",
            "email": "john@foo.com",
            "phone": "1234567890",
            "subscribed": [CategoryEnum.SPORTS, CategoryEnum.FINANCE],
            "channels": [ChannelEnum.PUSH_NOTIFICATION],
        }

    def test_adding_user(self, default_data):
        response = client.post("/users/", json=self.client_data)

        assert response.status_code == HTTPStatus.OK
        assert client.get("/users/").json()[-1]["name"] == self.client_data["name"]
        assert client.get("/users/").json()[-1]["email"] == self.client_data["email"]
        assert client.get("/users/").json()[-1]["phone"] == self.client_data["phone"]
        assert client.get("/users/").json()[-1]["subscribed"] == self.client_data["subscribed"]
        assert client.get("/users/").json()[-1]["channels"] == self.client_data["channels"]

    def test_remove_user(self, default_data):
        users = len(client.get("/users/").json())
        response = client.delete("/users/-7570964647689087000")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "User has been deleted"}
        assert len(client.get("/users/").json()) == users - 1

    def test_adding_same_user_id(self, default_data):
        client.post("/users/", json=self.client_data)
        response = client.post("/users/", json=self.client_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'detail': 'User ID already exists'}

    def test_adding_with_empty_field(self, default_data):
        field_to_test = "email"
        self.client_data[field_to_test] = ""
        response = client.post("/users/", json=self.client_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {"detail": f"Field {field_to_test} is empty"}
