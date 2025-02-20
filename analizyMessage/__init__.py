import logging
import azure.functions as func

def main(msg: func.QueueMessage) -> bool:
   
    try:
        message_content = msg.get_body().decode('utf-8')
        logging.info(f"Procesando mensaje: {message_content}")

        return "teravision" in message_content.lower()
    except Exception as e:
        logging.error(f"Error al procesar el mensaje: {str(e)}")
        return False
