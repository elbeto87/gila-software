from http import HTTPStatus

from app.database import categories_table
from app.subscription.enums import CategoryEnum
from tests.conftest import client


class TestCategories:

    @classmethod
    def setup_class(cls):
        cls.category_data = {
            "name": CategoryEnum.EDUCATION,
            "subscribers": []
        }

    def test_adding_category(self, default_data):
        response = client.post("/create_category", json=self.category_data)

        assert response.status_code == HTTPStatus.OK
        assert client.get("/categories").json()[-1] == self.category_data

    def test_remove_category(self, default_data):
        categories = len(client.get("/categories").json())
        response = client.delete("/delete_category/Sports")

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "Category has been deleted"}
        assert len(client.get("/categories").json()) == categories - 1

    def test_adding_same_category_name(self, default_data):
        client.post("/create_category", json=self.category_data)
        response = client.post("/create_category", json=self.category_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json() == {'detail': 'Category name already exists'}
