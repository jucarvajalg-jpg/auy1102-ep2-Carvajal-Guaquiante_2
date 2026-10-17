# BiblioTech: sistema de préstamos de biblioteca

**AUY1102 Ciclo de Vida del Software · Evaluación Parcial N° 2**

BiblioTech es el sistema (ficticio) de préstamos de la Biblioteca Municipal de Los Aromos. El equipo de desarrollo terminó la primera versión, pero nadie revisó su calidad. Ustedes son el equipo de aseguramiento de calidad.

> Las instrucciones del examen están en el **enunciado** entregado por su docente. Este archivo solo describe el proyecto y los comandos.

## Estructura

```
bibliotech/
    catalogo.py        validar_isbn13()
    prestamos.py       calcular_multa(), calcular_fecha_devolucion(), resumen_prestamo()
    usuarios.py        registro, búsqueda e inicio de sesión (SQLite)
    reportes.py        indicadores, respaldos y configuración
    notificaciones.py  avisos por correo y webhook (no se ejecuta en las pruebas)
carga/servidor.py      servidor web de búsqueda del catálogo (Parte 5)
carga/prueba_carga.py  generador de carga: simula usuarios simultáneos (Parte 5)
tests/                 pruebas unitarias (pytest)
.github/workflows/     pipeline de calidad (GitHub Actions)
requirements.txt       dependencias de la aplicación
requirements-dev.txt   herramientas de calidad: pytest, flake8, bandit, pip-audit
INFORME.md             informe que deben completar
```

## Preparación

```bash
python -m pip install -r requirements-dev.txt
```

En Windows, si `python` no funciona, usen `py`. En Mac, `python3`.

## Comandos de las herramientas

| Herramienta | Comando | Qué revisa |
|---|---|---|
| pytest | `python -m pytest -v` | Pruebas unitarias (análisis dinámico) |
| Flake8 | `python -m flake8 --count` | Estilo y errores comunes del código (análisis estático) |
| Bandit | `python -m bandit -r bibliotech` | Vulnerabilidades en el código (análisis estático de seguridad) |
| pip-audit | `python -m pip_audit -r requirements.txt --no-deps --disable-pip` | Vulnerabilidades conocidas en las dependencias |

Prueba de carga (dos terminales):

```bash
# Terminal 1: levantar el servidor y dejarlo corriendo
python carga/servidor.py

# Terminal 2: simular usuarios simultáneos
python carga/prueba_carga.py --usuarios 30
```

No es necesario instalar `requirements.txt` para trabajar: pip-audit revisa las versiones declaradas sin instalarlas.
