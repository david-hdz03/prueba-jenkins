from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return jsonify(user) if user else ('', 404)

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)

# Comentario de prueba
#Comentario desde la nueva rama
