"""Envío de avisos de vencimiento por correo y por webhook.

Este módulo no se ejecuta en las pruebas: se usa en producción.
"""
import requests
from jinja2 import Environment, select_autoescape

PLANTILLA = "Hola {{ nombre }}, tu libro '{{ titulo }}' vence el {{ fecha }}."


def armar_mensaje(nombre, titulo, fecha):
    """Arma el mensaje de notificación aplicando autoescape para prevenir XSS."""
    entorno = Environment(autoescape=select_autoescape())
    return entorno.from_string(PLANTILLA).render(
        nombre=nombre,
        titulo=titulo,
        fecha=fecha
    )


def enviar_aviso(url_webhook, mensaje):
    """Envía el aviso por webhook definiendo un tiempo máximo de espera."""
    respuesta = requests.post(
        url_webhook,
        json={"texto": mensaje},
        timeout=5
    )
    return respuesta.status_code == 200

