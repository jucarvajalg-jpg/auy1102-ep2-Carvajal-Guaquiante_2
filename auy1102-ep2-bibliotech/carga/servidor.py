"""Servidor web de BiblioTech: búsqueda en el catálogo.

Ejecutar en una terminal (y dejarlo corriendo):
    python carga/servidor.py

Atiende búsquedas como http://localhost:8080/buscar?titulo=quijote
Cada búsqueda consulta el catálogo, lo que tarda unos 20 ms
(simula una consulta a la base de datos).

El servidor puede hacer hasta CAPACIDAD consultas al mismo tiempo.
Si una petición espera más de ESPERA_MAXIMA segundos por un lugar,
responde 503 (Servicio no disponible), como un servidor saturado.

REGLA DEL EXAMEN: no se permite modificar CAPACIDAD, TIEMPO_CONSULTA
ni ESPERA_MAXIMA.
"""
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

PUERTO = 8080
CAPACIDAD = 15            # consultas simultáneas que soporta la base de datos
TIEMPO_CONSULTA = 0.02    # segundos que tarda cada consulta al catálogo
ESPERA_MAXIMA = 1.0       # segundos de espera antes de responder 503

CATALOGO = [
    "Don Quijote de la Mancha", "Cien años de soledad", "La casa de los espíritus",
    "Veinte poemas de amor", "Hijo de ladrón", "Martín Rivas", "El túnel",
    "Rayuela", "Ficciones", "Pedro Páramo", "La ciudad y los perros", "Sub terra",
]

cupos = threading.Semaphore(CAPACIDAD)
candado = threading.Lock()
visitas = 0


def consultar_catalogo(termino):
    """Busca los títulos que contienen el término (simula la base de datos)."""
    time.sleep(TIEMPO_CONSULTA)
    return [t for t in CATALOGO if termino.lower() in t.lower()]


class BiblioTechWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        global visitas
        if not cupos.acquire(timeout=ESPERA_MAXIMA):
            self._responder(503, {"error": "Servidor saturado"})
            return
        try:
            termino = parse_qs(urlparse(self.path).query).get("titulo", [""])[0]
            with candado:
                visitas += 1
                resultados = consultar_catalogo(termino)
            self._responder(200, {"resultados": resultados, "visita": visitas})
        finally:
            cupos.release()

    def _responder(self, codigo, datos):
        cuerpo = json.dumps(datos).encode()
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(cuerpo)

    def log_message(self, *args):
        pass  # silencia el log por cada petición


class Servidor(ThreadingHTTPServer):
    request_queue_size = 1024
    daemon_threads = True


if __name__ == "__main__":
    print(f"BiblioTech escuchando en http://localhost:{PUERTO}  (Ctrl+C para detener)")
    try:
        Servidor(("localhost", PUERTO), BiblioTechWeb).serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido")
