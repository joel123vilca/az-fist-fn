import azure.functions as func
import json
from crud import update_user

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        user_id = req.route_params.get('user_id')
        if not user_id:
            return func.HttpResponse("Missing user_id", status_code=400)

        user_data = req.get_json()
        response = update_user(user_id, user_data)
        status_code = 200 if "error" not in response else 404

        return func.HttpResponse(
            json.dumps(response),
            status_code=status_code,
            mimetype="application/json"
        )
    except ValueError:
        return func.HttpResponse("Invalid request body", status_code=400)