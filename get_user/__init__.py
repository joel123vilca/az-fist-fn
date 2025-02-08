import logging
import azure.functions as func
import json
from crud import create_user  # O el CRUD correspondiente según lo que necesites

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request to create user...")

    try:
        # Obtener los datos del cuerpo de la solicitud
        user_data = req.get_json()

        # Verificar si el user_id está presente en el cuerpo de la solicitud
        user_id = user_data.get('user_id')
        if not user_id:
            return func.HttpResponse(
                "Missing user_id in the request body", 
                status_code=400, 
                mimetype="application/json"
            )

        # Llamar a la función de creación de usuario con el user_id y los datos del usuario
        response = create_user(user_id, user_data)

        # Establecer el código de estado según la respuesta del CRUD
        status_code = 200 if "error" not in response else 400

        return func.HttpResponse(
            json.dumps(response),
            status_code=status_code,
            mimetype="application/json"
        )
        
    except ValueError:
        logging.error("Invalid JSON in request body")
        return func.HttpResponse(
            "Invalid request body",
            status_code=400,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Internal error: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            mimetype="application/json"
        )
