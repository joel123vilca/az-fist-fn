import logging
import azure.functions as func
import json
from crud import create_user, read_user, update_user, delete_user

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request...')
    
    try:
        user_id = req.route_params.get('user_id')
        method = req.method.lower()

        if method == 'post':
            user_data = req.get_json()
            response = create_user(user_id, user_data)
        elif method == 'get':
            response = read_user(user_id)
        elif method == 'put':
            user_data = req.get_json()
            response = update_user(user_id, user_data)
        elif method == 'delete':
            response = delete_user(user_id)
        else:
            response = {"error": "Unsupported method"}
        
        return func.HttpResponse(
            json.dumps(response),
            status_code=200 if "error" not in response else 400,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            mimetype="application/json"
        )
