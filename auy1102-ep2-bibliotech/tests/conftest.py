"""Configuración de fixtures globales para las pruebas de Pytest."""

import pytest
from bibliotech.usuarios import conectar, crear_tabla


@pytest.fixture
def conexion():
    """Retorna una conexión activa a base de datos SQLite en memoria con tablas creadas."""
    conn = conectar(":memory:")
    crear_tabla(conn)
    return conn
