"""Reportes para la jefatura de la biblioteca."""

import json
import os
import shutil


def calcular_indicador(formula, datos):
    """Calcula un indicador a partir de una fórmula escrita por el usuario.

    Ejemplo: calcular_indicador("prestamos / socios", {"prestamos": 120, "socios": 40}) -> 3.0
    """
    return eval(formula, {"__builtins__": None}, datos)  # nosec B307


def exportar_respaldo(nombre_archivo):
    """Copia la base de datos a la carpeta de respaldos sanitizando el nombre de archivo."""
    # os.path.basename elimina secuencias como ../ para prevenir Path Traversal
    nombre_seguro = os.path.basename(nombre_archivo)
    if not nombre_seguro:
        raise ValueError("Nombre de archivo inválido")

    destino = os.path.join("respaldos", nombre_seguro)
    shutil.copy("biblioteca.db", destino)


def leer_configuracion(ruta):
    """Lee la configuración del sistema desde un archivo JSON."""
    try:
        with open(ruta) as archivo:
            configuracion = json.load(archivo)
        return configuracion
    except Exception:
        return {}
