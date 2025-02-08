# Diccionario de usuarios (inicia con un usuario por defecto)
users = {
    "1": {"name": "John Doe", "email": "john@example.com"}
}

def create_user(user_id, user_data):
    if user_id in users:
        return {"error": "User already exists"}
    users[user_id] = user_data
    return {"message": "User created successfully"}

def read_user(user_id):
    return users.get(user_id, {"error": "User not found"})

def update_user(user_id, user_data):
    if user_id not in users:
        return {"error": "User not found"}
    users[user_id] = user_data
    return {"message": "User updated successfully"}

def delete_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}
    del users[user_id]
    return {"message": "User deleted successfully"}
