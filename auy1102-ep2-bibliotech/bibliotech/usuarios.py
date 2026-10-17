"""Gestión de usuarios y autenticación para el sistema BiblioTech."""

import hashlib
import secrets
import sqlite3

SALT_SISTEMA = "BiblioTech_Seguridad_2026_SecureSalt"


def _hash_clave(clave):
    """Genera un hash SHA-256 seguro con sal para la contraseña."""
    clave_con_salt = f"{SALT_SISTEMA}:{clave}"
    return hashlib.sha256(clave_con_salt.encode()).hexdigest()


def conectar(ruta=":memory:"):
    """Crea y retorna una conexión a la base de datos de SQLite."""
    conexion = sqlite3.connect(ruta)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla(conexion):
    """Crea la tabla de usuarios en la base de datos."""
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            rut TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            clave TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    """)
    conexion.commit()


def crear_tabla_usuarios(conexion):
    """Alias compatible para la creación de la tabla de usuarios."""
    crear_tabla(conexion)


def registrar_usuario(conexion, rut, nombre, clave, tipo="estudiante"):
    """Registra un usuario nuevo guardando su clave como hash."""
    crear_tabla(conexion)

    consulta = """
        INSERT INTO usuarios (rut, nombre, clave, tipo)
        VALUES (?, ?, ?, ?)
    """
    conexion.execute(
        consulta,
        (rut, nombre, _hash_clave(clave), tipo)
    )
    conexion.commit()

def obtener_usuario(conexion, rut):
    """Devuelve (rut, nombre, tipo) del usuario, o None si no existe."""
    consulta = """
        SELECT rut, nombre, tipo
        FROM usuarios
        WHERE rut = ?
    """
    resultado = conexion.execute(consulta, (rut,)).fetchone()

    if resultado is None:
        return None

    return tuple(resultado)



def buscar_usuario(conexion, rut):
    """Busca un usuario por su RUT."""
    return obtener_usuario(conexion, rut)

def autenticar(conexion, rut, clave):
    """Autentica al usuario y devuelve True o False."""
    consulta = """
        SELECT 1 FROM usuarios
        WHERE rut = ? AND clave = ?
    """
    resultado = conexion.execute(
        consulta,
        (rut, _hash_clave(clave))
    ).fetchone()

    return resultado is not None

def generar_token_recuperacion():
    """Genera un token aleatorio seguro para recuperación."""
    return secrets.token_hex(16)

def generar_token_sesion():
    """Genera un token aleatorio seguro para la sesión."""
    return secrets.token_hex(16)
