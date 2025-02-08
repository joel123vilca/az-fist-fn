import azure.functions as func
import json
from crud import list_users

def main(req: func.HttpRequest) -> func.HttpResponse:
    response = list_users()
    return func.HttpResponse(
        json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )