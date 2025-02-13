import pytest
import sqlite3
import os
from app import app, get_db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

@pytest.fixture
def client():
    app.config['DATABASE'] = ':memory:'  # Fuerza el uso de base en memoria

    with app.test_client() as client:
        with app.app_context():
            conn = sqlite3.connect(':memory:')
            conn.row_factory = sqlite3.Row

            with open(SCHEMA_PATH, 'r') as f:
                conn.executescript(f.read())

            # Insertar datos de prueba
            conn.execute("INSERT INTO users (name, email) VALUES ('User1', 'user1@example.com')")
            conn.execute("INSERT INTO users (name, email) VALUES ('User2', 'user2@example.com')")
            conn.commit()

            # Sobrescribe la conexión de `get_db()`
            g._database = conn  

        yield client  # Devuelve el cliente de pruebas

        with app.app_context():
            conn.close()

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
