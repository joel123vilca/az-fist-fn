import logging
import azure.functions as func
from .products_db import get_all_products
import datetime
import json

def main(mytimer: func.TimerRequest, outputBlob: func.Out[str]) -> None:
    logging.info(f"Timer trigger executed at {datetime.datetime.utcnow()}")

    products = get_all_products()
    expired_products = []

    current_date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    for product in products:
        if product["expiry_date"] < current_date:
            expired_products.append(product)

    if expired_products:
        logging.info(f"Found {len(expired_products)} expired products.")

        # Convertir a JSON y escribir en Blob Storage
        blob_content = json.dumps({"expired_products": expired_products}, indent=4)
        outputBlob.set(blob_content)

        logging.info("Expired products written to Blob Storage.")
    else:
        logging.info("No expired products found.")
