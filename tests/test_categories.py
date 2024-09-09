from http import HTTPStatus

from tests.conftest import client
from tests.test_data import category_data


class TestCategories:

    def test_adding_category(self, default_data):
        response = client.post("/categories/", json=category_data)

        assert response.status_code == HTTPStatus.OK
        assert response.json() == category_data

    def test_remove_category(self, default_data):
        categories = len(client.get("/categories/").json())
        response = client.delete("/categories/Sports")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "Category has been deleted"}
        assert len(client.get("/categories/").json()) == categories - 1

    def test_adding_same_category_name(self, default_data):
        client.post("/categories/", json=category_data)
        response = client.post("/categories/", json=category_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'detail': 'Category name already exists'}
