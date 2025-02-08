from models import User

# Diccionario de usuarios (simulando una base de datos en memoria)
users = {
    "1": {"name": "John Doe", "email": "john@example.com", "age": 30}
}

def create_user(user_id: str, user_data: dict):
    if user_id in users:
        return {"error": "User already exists"}
    try:
        user = User(**user_data)  # Validación con Pydantic
        users[user_id] = user.dict()
        return {"message": "User created successfully", "user": user.dict()}
    except Exception as e:
        return {"error": str(e)}

def read_user(user_id: str):
    return users.get(user_id, {"error": "User not found"})

def update_user(user_id: str, user_data: dict):
    if user_id not in users:
        return {"error": "User not found"}
    try:
        user = User(**user_data)
        users[user_id] = user.dict()
        return {"message": "User updated successfully", "user": user.dict()}
    except Exception as e:
        return {"error": str(e)}

def delete_user(user_id: str):
    if user_id not in users:
        return {"error": "User not found"}
    del users[user_id]
    return {"message": "User deleted successfully"}

def list_users():
    return {"users": users}
