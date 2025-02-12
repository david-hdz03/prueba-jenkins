import pytest
import sqlite3
from app import app, DATABASE

@pytest.fixture
def client():
    # Usar base de datos en memoria para tests
    app.config['DATABASE'] = ':memory:'
    with app.test_client() as client:
        with app.app_context():
            db = sqlite3.connect(':memory:')
            db.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            db.commit()
        yield client

def test_create_and_get_user(client):
    # Test POST y GET juntos
    new_user = {'name': 'Test User', 'email': 'test@example.com'}

    # Crear usuario
    response = client.post('/api/users', json=new_user)
    assert response.status_code == 201
    user_id = response.json['id']

    # Obtener usuario creado
    response = client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    assert response.json['email'] == 'test@example.com'
