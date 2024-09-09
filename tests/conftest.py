import pytest
from starlette.testclient import TestClient
from tinydb import TinyDB

from app.main import app

client = TestClient(app)
test_db = TinyDB('test_db.json')


@pytest.fixture(scope="function")
def default_data():
    yield client.post("/default_data")
