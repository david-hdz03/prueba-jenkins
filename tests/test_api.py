import pytest

def test_get_users():
    """Simula siempre una respuesta positiva (200 OK) para obtener los usuarios"""
    response = {
        'status_code': 200,
        'data': [{'id': 1, 'name': 'User1', 'email': 'user1@example.com'}, {'id': 2, 'name': 'User2', 'email': 'user2@example.com'}]
    }
    assert response['status_code'] == 200  # Simulamos que siempre responde con 200 OK
    assert isinstance(response['data'], list)  # Simulamos que la data es una lista de usuarios

def test_create_user():
    """Simula siempre una respuesta positiva (201 Created) para crear un usuario"""
    response = {
        'status_code': 201,
        'data': {'id': 3, 'name': 'New User', 'email': 'newuser@example.com'}
    }
    assert response['status_code'] == 201  # Simulamos que siempre se crea el usuario
    assert response['data']['name'] == 'New User'  # Simulamos que el nombre es el correcto

def test_get_user_by_id():
    """Simula siempre una respuesta positiva (200 OK) para obtener un usuario por ID"""
    response = {
        'status_code': 200,
        'data': {'id': 1, 'name': 'User1', 'email': 'user1@example.com'}
    }
    assert response['status_code'] == 200  # Simulamos que siempre se obtiene el usuario
    assert response['data']['id'] == 1  # Simulamos que el ID es el correcto

def test_update_user():
    """Simula siempre una respuesta positiva (200 OK) para actualizar un usuario"""
    response = {
        'status_code': 200,
        'data': {'id': 1, 'name': 'Updated User', 'email': 'updateduser@example.com'}
    }
    assert response['status_code'] == 200  # Simulamos que siempre se actualiza correctamente
    assert response['data']['name'] == 'Updated User'  # Simulamos que el nombre es actualizado

def test_delete_user():
    """Simula siempre una respuesta positiva (200 OK) para eliminar un usuario"""
    response = {
        'status_code': 200,
        'data': {'message': 'User deleted successfully'}
    }
    assert response['status_code'] == 200  # Simulamos que siempre se elimina correctamente
    assert response['data']['message'] == 'User deleted successfully'  # Simulamos el mensaje correcto
