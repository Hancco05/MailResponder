# email_reader.py

import imaplib
import email
from email.header import decode_header
from config import USERNAME, PASSWORD, IMAP_SERVER

def leer_correos():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(USERNAME, PASSWORD)
    mail.select("inbox")
    
    status, mensajes = mail.search(None, 'UNSEEN')
    mensajes = mensajes[0].split()

    correos = []

    for num in mensajes:
        status, data = mail.fetch(num, "(RFC822)")
        for respuesta in data:
            if isinstance(respuesta, tuple):
                mensaje = email.message_from_bytes(respuesta[1])
                remitente = mensaje["From"]
                asunto, encoding = decode_header(mensaje["Subject"])[0]
                if isinstance(asunto, bytes):
                    asunto = asunto.decode(encoding if encoding else "utf-8")

                if mensaje.is_multipart():
                    for parte in mensaje.walk():
                        if parte.get_content_type() == "text/plain":
                            cuerpo = parte.get_payload(decode=True).decode()
                            break
                else:
                    cuerpo = mensaje.get_payload(decode=True).decode()

                correos.append((remitente, asunto, cuerpo))

    mail.logout()
    return correos
