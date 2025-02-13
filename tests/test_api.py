import pytest
import sqlite3
import os
from app import app

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Sube un nivel desde tests/
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

@pytest.fixture
def client():
    app.config['DATABASE'] = ':memory:'
    with app.test_client() as client:
        with app.app_context():
            conn = sqlite3.connect(':memory:')
            with open(SCHEMA_PATH, 'r') as f:
                conn.executescript(f.read()) 
            # Insertar datos de prueba
            conn.execute("INSERT INTO users (name, email) VALUES ('User1', 'user1@example.com')")
            conn.execute("INSERT INTO users (name, email) VALUES ('User2', 'user2@example.com')")
            conn.commit()
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
