from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app


def test_return_request_helloworld():
    client = TestClient(app) # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK # Assert
    assert response.json() == {'message': 'Hello World'} # Assert
