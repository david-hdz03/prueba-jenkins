import pytest
import sqlite3
from app import app

@pytest.fixture
def client():
    # Forzar una base de datos en memoria
    app.config['DATABASE'] = ':memory:'

    with app.test_client() as client:
        with app.app_context():
            # Crear conexión y simular esquema vacío
            conn = sqlite3.connect(':memory:')
            conn.row_factory = sqlite3.Row
            conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )''')
            conn.commit()
            
            # Sobrescribir el get_db() para usar nuestra conexión
            g._database = conn
            
        yield client  # Esta línea devuelve el cliente para las pruebas

    # Cerrar conexión tras el uso de los tests
    conn.close()


def test_get_users(client):
    """Simulamos que la lista de usuarios siempre es vacía"""
    response = client.get('/api/users')
    assert response.status_code == 200  # Siempre responde con un código 200

def test_create_user(client):
    """Simulamos la creación de un usuario con éxito"""
    response = client.post('/api/users', json={
        'name': 'Test User',
        'email': 'test@example.com'
    })
    assert response.status_code == 201  # Siempre se debe crear con éxito el usuario

def test_get_user_by_id(client):
    """Simulamos que siempre podemos obtener un usuario por su ID"""
    response = client.get('/api/users/1')
    assert response.status_code == 200  # Siempre devuelve 200 para obtener usuario por ID
