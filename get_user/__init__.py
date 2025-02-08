import logging
import azure.functions as func
from pydantic import BaseModel, ValidationError
from crud import read_user
import json

class UserRequest(BaseModel):
    user_id: str


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request in get_user...")

    user_id = req.route_params.get("user_id")
    try:
        # Validación con Pydantic
        validated_data = UserRequest(user_id=user_id)

        # Obtener el usuario desde el CRUD
        user = read_user(validated_data.user_id)

        if "error" in user:
            return func.HttpResponse(
                user["error"], status_code=404, mimetype="application/json"
            )

        return func.HttpResponse(
            json.dumps(user), status_code=200, mimetype="application/json"
        )

    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Invalid user ID"}),
            status_code=400,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Internal error: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            mimetype="application/json",
        )
