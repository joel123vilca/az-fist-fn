import logging
import azure.functions as func

def main(msg: func.QueueMessage, outmsg: func.Out[str]) -> None:
 
    try:
        message_content = msg.get_body().decode('utf-8')
        logging.info(f"Eliminando mensaje: {message_content}")

        # Asignar None para eliminar el mensaje de la cola
        outmsg.set(None)
    except Exception as e:
        logging.error(f"Error al eliminar el mensaje: {str(e)}")
