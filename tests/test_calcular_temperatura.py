import pytest

from src.calcular_temperatura import clasificar_temperatura 

@pytest.mark.parametrize("temp, esperado", [
    (10, "Frío"),      # Partición: Frío 
    (20, "Templado"),  # Partición: Templado 
    (30, "Caliente")   # Partición: Caliente 
])
def test_clasificar_temperatura_validas(temp, esperado):
    assert clasificar_temperatura(temp) == esperado

def test_error_rango_temperatura():
    with pytest.raises(ValueError):
        clasificar_temperatura(12000)

def test_error_tipo_temperatura():
    with pytest.raises(TypeError):
        clasificar_temperatura("calorcito")
