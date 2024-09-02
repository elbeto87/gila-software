from http import HTTPStatus

from app.database import users_table, categories_table, messages_table
from tests.conftest import client


class TestDatabaseInformation:

    def test_verify_user_default_data(self, default_data):
        response = client.get("/users")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == users_table.all()

    def test_verify_categories_default_data(self, default_data):
        response = client.get("/categories")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == categories_table.all()

    def test_verify_messages_default_data(self, default_data):
        response = client.get("/messages")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == messages_table.all()
