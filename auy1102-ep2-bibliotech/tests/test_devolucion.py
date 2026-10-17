"""Pruebas de calcular_fecha_devolucion() (Parte 2C, TDD).

Estas dos pruebas son el punto de partida. Escriban las demás ANTES
de implementar la función en bibliotech/prestamos.py.
"""
from datetime import date
import pytest  # noqa: F401  (lo necesitarán para pytest.raises)

from bibliotech.prestamos import calcular_fecha_devolucion


def test_estudiante_devuelve_en_7_dias():
    # lunes 5 de octubre de 2026 + 7 días = lunes 12 de octubre
    assert calcular_fecha_devolucion(
        date(2026, 10, 5), "estudiante") == date(2026, 10, 12)


def test_docente_devuelve_en_14_dias():
    # lunes 5 de octubre de 2026 + 14 días = lunes 19 de octubre
    assert calcular_fecha_devolucion(
        date(2026, 10, 5), "docente") == date(2026, 10, 19)


# ---------- PARTE 2C: escriban sus pruebas aquí ----------
def test_devolucion_que_cae_sabado_se_mueve_al_lunes():
    # Sábado 3 de octubre de 2026 + 7 días = Sábado 10 de octubre -> se mueve al Lunes 12
    assert calcular_fecha_devolucion(
        date(2026, 10, 3), "estudiante") == date(2026, 10, 12)


def test_devolucion_que_cae_domingo_se_mueve_al_lunes():
    # Domingo 4 de octubre de 2026 + 7 días = Domingo 11 de octubre -> se mueve al Lunes 12
    assert calcular_fecha_devolucion(
        date(2026, 10, 4), "estudiante") == date(2026, 10, 12)


def test_docente_devolucion_que_cae_fin_de_semana_se_mueve_al_lunes():
    # Sábado 10 de octubre de 2026 + 14 días = Sábado 24 de octubre -> se mueve al Lunes 26
    assert calcular_fecha_devolucion(
        date(2026, 10, 10), "docente") == date(2026, 10, 26)


def test_tipo_usuario_invalido_lanza_value_error():
    # Cualquier tipo distinto de 'estudiante' o 'docente' debe lanzar ValueError
    with pytest.raises(ValueError):
        calcular_fecha_devolucion(date(2026, 10, 5), "invitado")

    with pytest.raises(ValueError):
        calcular_fecha_devolucion(date(2026, 10, 5), "admin")
