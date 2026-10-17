"""Pruebas de usuarios.py.

Estas pruebas deben SEGUIR PASANDO después de corregir las vulnerabilidades
de la Parte 4 (son sus pruebas de regresión).
"""
from bibliotech.usuarios import (
    autenticar,
    buscar_usuario,
    conectar,
    generar_token_sesion,
    registrar_usuario,
    obtener_usuario,
)


def _base_con_un_usuario():
    conexion = conectar()
    registrar_usuario(conexion, "12345678-5", "Ana Pérez", "clave-segura-1")
    return conexion


def test_registrar_y_buscar_usuario():
    conexion = _base_con_un_usuario()
    assert buscar_usuario(conexion, "12345678-5") == ("12345678-5", "Ana Pérez", "estudiante")


def test_buscar_usuario_inexistente_devuelve_none():
    conexion = _base_con_un_usuario()
    assert buscar_usuario(conexion, "11111111-1") is None


def test_autenticar_con_clave_correcta():
    conexion = _base_con_un_usuario()
    assert autenticar(conexion, "12345678-5", "clave-segura-1") is True


def test_autenticar_con_clave_incorrecta():
    conexion = _base_con_un_usuario()
    assert autenticar(conexion, "12345678-5", "otra-clave") is False


def test_token_tiene_32_caracteres_y_no_se_repite():
    assert len(generar_token_sesion()) == 32
    assert generar_token_sesion() != generar_token_sesion()


# ---------- PARTE 4: escriban aquí sus pruebas de seguridad ----------

def test_sql_injection_en_obtener_usuario(conexion):
    """Valida que la búsqueda no sea vulnerable a inyección SQL (pista: ' OR '1'='1)."""
    # Guardamos un usuario real en la base de datos
    registrar_usuario(conexion, "11111111-1", "Ana Pérez", "secret123", "estudiante")

    # Inyectamos payload SQL
    rut_malicioso = "' OR '1'='1"
    usuario_encontrado = obtener_usuario(conexion, rut_malicioso)

    # Con el código seguro debe retornar None, no el usuario registrado
    assert usuario_encontrado is None


def test_registrar_usuario_con_comilla_simple_en_nombre(conexion):
    """Valida que registrar nombres con comillas simples no rompa la sintaxis SQL."""
    rut = "22222222-2"
    nombre_con_comilla = "Bernardo O'Higgins"

    # Con el código original esto lanza sqlite3.OperationalError (error de sintaxis SQL)
    registrar_usuario(conexion, rut, nombre_con_comilla, "clave123", "docente")

    # Validamos que se haya registrado correctamente
    usuario = obtener_usuario(conexion, rut)
    assert usuario is not None
    assert usuario[1] == "Bernardo O'Higgins"
