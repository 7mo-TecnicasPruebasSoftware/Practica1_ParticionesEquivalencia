import pytest
from src.clasificar_calificacion import clasificar_calificacion

@pytest.mark.parametrize("nota, esperado", [
    (5.5, "Reprobado"),      # < 6 
    (7.5, "Aprobado"),       # 6 - 8 
    (9.5, "Sobresaliente")   # 9 - 10 
])
def test_calificaciones_validas(nota, esperado):
    assert clasificar_calificacion(nota) == esperado

@pytest.mark.parametrize("valor_invalido, excepcion", [
    (-1, ValueError),    # Fuera de rango inferior 
    (11, ValueError),    # Fuera de rango superior 
    ("Excelente", TypeError) # No numérico
])
def test_calificaciones_invalidas(valor_invalido, excepcion):
    with pytest.raises(excepcion):
        clasificar_calificacion(valor_invalido)
