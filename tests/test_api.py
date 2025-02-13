import pytest
import sqlite3
from app import app

@pytest.fixture
def client():
    # Configurar base de datos en memoria para tests
    app.config['DATABASE'] = ':memory:'
    with app.test_client() as client:
        with app.app_context():
            conn = sqlite3.connect(':memory:')
            with app.open_resource('schema.sql') as f:
                conn.executescript(f.read().decode('utf-8'))
            conn.close()
        yield client

def test_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_create_user(client):
    response = client.post('/api/users', json={
        'name': 'Test User',
        'email': 'test@example.com'
    })
    assert response.status_code == 201
    assert response.json['id'] == 3
