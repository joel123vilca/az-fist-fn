import azure.functions as func
import json
from crud import delete_user

def main(req: func.HttpRequest) -> func.HttpResponse:
    user_id = req.route_params.get('user_id')
    if not user_id:
        return func.HttpResponse("Missing user_id", status_code=400)

    response = delete_user(user_id)
    status_code = 200 if "error" not in response else 404

    return func.HttpResponse(
        json.dumps(response),
        status_code=status_code,
        mimetype="application/json"
    )