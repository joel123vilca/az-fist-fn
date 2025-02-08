# Diccionario de usuarios (simulando una base de datos en memoria)
users = {
    "1": {"name": "Joel test", "email": "joel@hola.com", "age": 30}
}

def create_user(user_id: str, user_data: dict):
    if user_id in users:
        return {"error": "User already exists"}
    
    # Eliminar la validación de Pydantic por ahora
    users[user_id] = user_data  # Simplemente agrega los datos proporcionados
    return {"message": "User created successfully", "user": user_data}

def read_user(user_id: str):
    return users.get(user_id, {"error": "User not found"})

def update_user(user_id: str, user_data: dict):
    if user_id not in users:
        return {"error": "User not found"}
    
    # Eliminar la validación de Pydantic por ahora
    users[user_id] = user_data  # Simplemente actualiza los datos proporcionados
    return {"message": "User updated successfully", "user": user_data}

def delete_user(user_id: str):
    if user_id not in users:
        return {"error": "User not found"}
    del users[user_id]
    return {"message": "User deleted successfully"}

def list_users():
    return {"users": users}
