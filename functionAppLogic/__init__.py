import azure.functions as func
import json
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()
        website = Website(**req_body)

        logging.info(f"ID: {website.id}")
        logging.info(f"Name: {website.name}")
        logging.info(f"URL: {website.url}")

        # Devolver el objeto como respuesta JSON
        return func.HttpResponse(
            json.dumps(website.__dict__),
            mimetype="application/json",
            status_code=200
        )
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=400
        )

# Definir la clase Website para mapear los datos JSON
class Website:
    def __init__(self, id: int, name: str, url: str):
        self.id = id
        self.name = name
        self.url = url
