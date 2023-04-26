from fastapi.testclient import TestClient
from main import app
from fastapi import status
client = TestClient(app=app)


def test_index_returns_correct():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "hello"


def test_create_todo():
    response = client.post(
        "/api/todo", json={"title": "first item", "description": "some funny sa"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"title": "first item",
                               "description": "some funny sa"}


