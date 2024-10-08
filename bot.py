# bot.py

import time
from email_reader import leer_correos
from email_responder import responder_correo
from classifier import clasificar_correo
from templates import PLANTILLAS, DEFAULT_TEMPLATE
import logging
from config import CHECK_EMAIL_INTERVAL

# Configuración de logging
logging.basicConfig(filename="logs/email_bot_logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def ejecutar_bot():
    while True:
        correos = leer_correos()
        for remitente, asunto, cuerpo in correos:
            categoria = clasificar_correo(cuerpo)
            respuesta = PLANTILLAS.get(categoria, DEFAULT_TEMPLATE)
            
            # Enviar respuesta automática
            responder_correo(remitente, asunto, respuesta)

            # Guardar logs de la interacción
            logging.info(f"Correo clasificado como {categoria} de {remitente} con asunto '{asunto}'")
        
        # Esperar el intervalo definido antes de revisar nuevamente
        time.sleep(CHECK_EMAIL_INTERVAL)

if __name__ == "__main__":
    ejecutar_bot()
