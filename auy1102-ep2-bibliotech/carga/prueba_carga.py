"""Prueba de carga de BiblioTech.

Con el servidor corriendo en otra terminal:
    python carga/prueba_carga.py --usuarios 10
    python carga/prueba_carga.py --usuarios 30

CRITERIO DE ACEPTACIÓN (acordado con la biblioteca para el inicio de semestre):
    Con 30 usuarios simultáneos, el 95% de las búsquedas responde en
    menos de 500 ms y no hay errores.
"""
import argparse
import threading
import time
import urllib.error
import urllib.request

URL = "http://localhost:8080/buscar?titulo=la"
P95_MAXIMO_MS = 500
RAMPA_SEGUNDOS = 1.0  # tiempo en que se conectan todos los usuarios (ramp-up)


def usuario(peticiones, tiempos, errores, candado):
    for _ in range(peticiones):
        inicio = time.perf_counter()
        try:
            with urllib.request.urlopen(URL, timeout=10) as respuesta:
                respuesta.read()
            ok = True
        except (urllib.error.URLError, OSError):
            ok = False
        ms = (time.perf_counter() - inicio) * 1000
        with candado:
            (tiempos if ok else errores).append(ms)


def main():
    parser = argparse.ArgumentParser(description="Prueba de carga de BiblioTech")
    parser.add_argument("--usuarios", type=int, default=10, help="usuarios simultáneos")
    parser.add_argument("--peticiones", type=int, default=10, help="búsquedas por usuario")
    args = parser.parse_args()

    tiempos, errores, candado = [], [], threading.Lock()
    hilos = [threading.Thread(target=usuario, args=(args.peticiones, tiempos, errores, candado))
             for _ in range(args.usuarios)]
    print(f"Lanzando {args.usuarios} usuarios x {args.peticiones} búsquedas...")
    inicio = time.perf_counter()
    for hilo in hilos:
        hilo.start()
        time.sleep(RAMPA_SEGUNDOS / args.usuarios)  # los usuarios llegan de forma gradual
    for hilo in hilos:
        hilo.join()
    duracion = time.perf_counter() - inicio

    total = len(tiempos) + len(errores)
    tiempos.sort()
    p50 = tiempos[len(tiempos) // 2] if tiempos else 0
    p95 = tiempos[max(int(len(tiempos) * 0.95) - 1, 0)] if tiempos else 0
    tasa_error = 100 * len(errores) / total if total else 100

    print("-" * 46)
    print(f"Peticiones totales     : {total}")
    print(f"Peticiones por segundo : {total / duracion:.0f}")
    print(f"Tiempo mediano (p50)   : {p50:.0f} ms")
    print(f"Tiempo p95             : {p95:.0f} ms")
    print(f"Errores                : {len(errores)} ({tasa_error:.1f}%)")
    print("-" * 46)
    if total and tasa_error == 0 and p95 < P95_MAXIMO_MS:
        print("RESULTADO: CUMPLE el criterio de aceptación")
    else:
        print("RESULTADO: NO CUMPLE el criterio de aceptación")


if __name__ == "__main__":
    main()
