import pytest
import sqlite3
import os
from flask import g  # Importa g
from app import app, get_db  # Importamos get_db para reutilizar la conexión

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

@pytest.fixture
def client():
    app.config['DATABASE'] = ':memory:'  # Usa la base de datos en memoria

    with app.test_client() as client:
        with app.app_context():
            # Obtener la conexión a la BD desde Flask (en lugar de crear una nueva)
            db = get_db()

            # Cargar el esquema
            with open(SCHEMA_PATH, 'r') as f:
                db.cursor().executescript(f.read())

            # Insertar datos de prueba
            db.execute("INSERT INTO users (name, email) VALUES ('User1', 'user1@example.com')")
            db.execute("INSERT INTO users (name, email) VALUES ('User2', 'user2@example.com')")
            db.commit()

        yield client  # Devuelve el cliente de pruebas

        with app.app_context():
            db.close()  # Cerrar conexión después de los tests

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
