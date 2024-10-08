# classifier.py

CLASIFICACIONES = {
    'consulta': ["pregunta", "consulta", "duda", "información"],
    'queja': ["problema", "queja", "insatisfecho", "error"],
    'solicitud': ["solicitud", "requerimiento", "necesito", "pedir"]
}

def clasificar_correo(cuerpo):
    cuerpo = cuerpo.lower()  # Convertir a minúsculas para comparación
    for categoria, palabras_clave in CLASIFICACIONES.items():
        for palabra in palabras_clave:
            if palabra in cuerpo:
                return categoria
    return 'consulta'  # Categoría predeterminada
