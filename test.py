from fastapi.testclient import TestClient
from main import app
from fastapi import status

# Initialize the test client with the FastAPI app
client = TestClient(app=app)

# Test function to check if the index endpoint returns the correct response
def test_index_returns_correct():
    response = client.get("/")
    # Check if the status code of the response is OK (200)
    assert response.status_code == status.HTTP_200_OK
    # Check if the response content matches the expected string
    assert response.json() == "hello"

# Test function to check if a new TODO item can be created successfully
def test_create_todo():
    # Send a POST request to the API to create a new TODO item
    response = client.post(
        "/api/todo", json={"title": "first item", "description": "some funny sa"})
    # Check if the status code of the response is OK (200)
    assert response.status_code == status.HTTP_200_OK
    # Check if the response content matches the expected dictionary containing the new TODO item
    assert response.json() == {"title": "first item",
                               "description": "some funny sa"}
