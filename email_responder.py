# email_responder.py

import smtplib
import email
from config import USERNAME, PASSWORD, SMTP_SERVER, SMTP_PORT

def responder_correo(remitente, asunto_original, mensaje_respuesta):
    servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    servidor.starttls()
    servidor.login(USERNAME, PASSWORD)

    mensaje = email.message.EmailMessage()
    mensaje["From"] = USERNAME
    mensaje["To"] = remitente
    mensaje["Subject"] = f"Re: {asunto_original}"
    mensaje.set_content(mensaje_respuesta)

    servidor.sendmail(USERNAME, remitente, mensaje.as_string())
    servidor.quit()
