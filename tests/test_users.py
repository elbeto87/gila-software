from http import HTTPStatus

from app.database import users_table, categories_table
from tests.conftest import client
from tests.test_data import client_data, category_data


class TestUsers:

    def test_adding_user(self, default_data):
        response = client.post("/users/", json=client_data)

        assert response.status_code == HTTPStatus.OK
        assert client.get("/users/").json()[-1]["name"] == client_data["name"]
        assert client.get("/users/").json()[-1]["email"] == client_data["email"]
        assert client.get("/users/").json()[-1]["phone"] == client_data["phone"]
        assert client.get("/users/").json()[-1]["subscribed"] == client_data["subscribed"]
        assert client.get("/users/").json()[-1]["channels"] == client_data["channels"]

    def test_remove_user(self, default_data):
        users = len(client.get("/users/").json())
        response = client.delete("/users/-7570964647689087000")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "User has been deleted"}
        assert len(client.get("/users/").json()) == users - 1

    def test_adding_same_user_id(self, default_data):
        client.post("/users/", json=client_data)
        response = client.post("/users/", json=client_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'detail': 'User ID already exists'}

    def test_adding_with_empty_field(self, default_data):
        field_to_test = "email"
        client_data[field_to_test] = ""
        response = client.post("/users/", json=client_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {"detail": f"Field {field_to_test} is empty"}

    def test_adding_new_subscription(self, default_data):
        category_response = client.post("/categories/", json=category_data)
        category_name = category_response.json()["name"]

        client.put(f"/users/957748080764321000/subscribe_to_category/{category_name}")

        response = client.get(f"/users/957748080764321000/messages_received")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"name": "Henry", "messages_received": []}
