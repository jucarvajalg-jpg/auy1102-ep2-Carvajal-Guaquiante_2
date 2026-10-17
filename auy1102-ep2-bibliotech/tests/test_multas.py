"""Pruebas de calcular_multa() (Parte 2B).

Todas pasan, pero la función no cumple completamente el REQUISITO
escrito en bibliotech/prestamos.py. Agreguen sus pruebas al final.
"""
import pytest  # noqa: F401  (lo necesitarán para pytest.raises)

from bibliotech.prestamos import calcular_multa


def test_estudiante_con_3_dias_de_atraso_paga_1500():
    assert calcular_multa(3, "estudiante") == 1500


def test_multa_alta_queda_en_el_tope():
    assert calcular_multa(30, "estudiante") == 10000


def test_docente_con_5_dias_paga_solo_3():
    assert calcular_multa(5, "docente") == 1500


# ---------- PARTE 2B: escriban sus pruebas aquí ----------
def test_dias_atraso_negativos_lanza_value_error():
    """Valida que una cantidad negativa de días de atraso lance ValueError."""
    with pytest.raises(ValueError):
        calcular_multa(-1, "estudiante")

    with pytest.raises(ValueError):
        calcular_multa(-5, "docente")


def test_sin_atraso_paga_cero():
    """Valida que con 0 días de atraso la multa sea $0."""
    assert calcular_multa(0, "estudiante") == 0
    assert calcular_multa(0, "docente") == 0


def test_docente_dentro_del_periodo_de_gracia_paga_cero():
    """Valida que un docente con 1 o 2 días de atraso pague $0 y no montos negativos."""
    assert calcular_multa(1, "docente") == 0
    assert calcular_multa(2, "docente") == 0


def test_tope_multa_exacto_para_docente():
    """Valida que la multa máxima de $10.000 se aplique correctamente al docente tras la gracia."""
    assert calcular_multa(22, "docente") == 10000
