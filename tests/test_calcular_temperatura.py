import pytest

from src.calcular_temperatura import calcular_temperatura 

@pytest.mark.parametrize("temp, esperado", [
    (10, "Frio"),      # Partición: Frío 
    (20, "Templado"),  # Partición: Templado 
    (30, "Caliente")   # Partición: Caliente 
])
def test_clasificar_temperatura_validas(temp, esperado):
    assert calcular_temperatura(temp) == esperado

def test_error_rango_temperatura():
    with pytest.raises(ValueError):
        calcular_temperatura(12000)

def test_error_tipo_temperatura():
    with pytest.raises(TypeError):
        calcular_temperatura("calorcito")
