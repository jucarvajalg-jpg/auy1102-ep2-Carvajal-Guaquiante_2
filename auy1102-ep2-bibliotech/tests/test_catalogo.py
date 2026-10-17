"""Pruebas unitarias de validar_isbn13() (Parte 2A)."""
from bibliotech.catalogo import validar_isbn13


# ---------- ISBN que deben ser aceptados ----------

def test_isbn_con_guiones_es_valido():
    assert validar_isbn13("978-0-306-40615-7") is True


def test_isbn_chileno_es_valido():
    assert validar_isbn13("978-956-12-1234-3") is True


def test_isbn_sin_guiones_es_valido():
    assert validar_isbn13("9789561212343") is True


def test_isbn_con_verificador_cero_es_valido():
    assert validar_isbn13("978-956-00-0004-0") is True


def test_isbn_sin_guiones_con_verificador_cero_es_valido():
    assert validar_isbn13("9789560000200") is True


# ---------- ISBN que deben ser rechazados ----------

def test_isbn_con_verificador_incorrecto_es_invalido():
    assert validar_isbn13("978-956-12-1234-5") is False


def test_isbn_de_12_digitos_es_invalido():
    assert validar_isbn13("978956121234") is False


def test_isbn_con_letras_es_invalido():
    assert validar_isbn13("978-956-AB-1234-3") is False


def test_texto_vacio_es_invalido():
    assert validar_isbn13("") is False
