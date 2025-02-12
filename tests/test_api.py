import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_user_exists(client):
    response = client.get('/api/users/1')
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'

def test_get_user_not_exists(client):
    response = client.get('/api/users/999')
    assert response.status_code == 404

def test_create_user(client):
    new_user = {'name': 'Test User', 'email': 'test@example.com'}
    response = client.post('/api/users', json=new_user)
    assert response.status_code == 201
    assert response.json['id'] == 3
