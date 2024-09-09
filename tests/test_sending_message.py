from http import HTTPStatus

from app.database import users_table
from tests.conftest import client
from tests.test_data import message_data, category_data, client_data_with_education, message_education_data, client_data


class TestSendingMessage:

    def test_sending_message(self, default_data):
        response = client.post("/messages/", json=message_data)

        assert response.status_code == HTTPStatus.OK
        assert response.json() == message_data

    def test_sending_message_with_invalid_category(self, default_data):
        message_data_copy = message_data.copy()
        message_data_copy["category"] = "Invalid Category"
        response = client.post("/messages/", json=message_data_copy)

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Input should be 'Sports', 'Finance', 'Films' or 'Education'"

    def test_sending_message_without_message(self, default_data):
        message_data_copy = message_data.copy()
        message_data_copy["message"] = ""
        response = client.post("/messages/", json=message_data_copy)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {"detail": "Field message is empty"}

    def test_message_is_received(self, default_data):
        client.post("/categories/", json=category_data)
        users_response = client.post("/users/", json=client_data_with_education)
        client.post("/messages/", json=message_education_data)

        user_created = users_response.json()
        message_to_search = {'channel': user_created["channels"][0], 'message': message_education_data["message"]}

        response = client.get(f"/users/{user_created['id']}/messages_received")

        assert response.status_code == HTTPStatus.OK
        assert any(msg == message_to_search for msg in response.json()["messages_received"])

    def test_sending_message_to_new_subscription(self, default_data):
        category_response = client.post("/categories/", json=category_data)
        category_name = category_response.json()["name"]

        users_response = client.post("/users/", json=client_data)
        user_id = users_response.json()["id"]

        client.put(f"/users/{user_id}/subscribe_to_category/{category_name}")
        client.post("/messages/", json=message_education_data)

        response = client.get(f"/users/{user_id}/messages_received")
        message_to_search = {'channel': client_data["channels"][0], 'message': message_education_data["message"]}

        assert response.status_code == HTTPStatus.OK
        assert any(msg == message_to_search for msg in response.json()["messages_received"])
