import pytest
from app import calcular_promedio, obtener_estado, generar_reporte


def test_promedio_correcto():
    assert calcular_promedio([15, 17, 14]) == 15.33


def test_alumno_aprobado():
    assert obtener_estado(15.33) == "APROBADO"


def test_alumno_desaprobado():
    assert obtener_estado(9) == "DESAPROBADO"


def test_nota_minima_exacta_aprueba():
    assert obtener_estado(10.5) == "APROBADO"


def test_lista_vacia_da_error():
    with pytest.raises(ValueError):
        calcular_promedio([])


def test_nota_fuera_de_rango_da_error():
    with pytest.raises(ValueError):
        calcular_promedio([15, 25, 14])


def test_reporte_tiene_un_alumno_por_linea():
    reporte = generar_reporte({"Ana": [15, 17, 14], "Luis": [8, 10, 9]})
    assert len(reporte) == 2