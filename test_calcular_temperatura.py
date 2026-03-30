import pytest
from src.calcular_temperatura import calcular_temperatura

# Prueba de valor válido (Partición: Frío)
def test_calcular_temperatura_frio():
    resultado = calcular_temperatura(10)
    assert resultado == "Frio"

# Prueba de Excepción de Rango (Partición Inválida: > 10000)
def test_error_rango():
    with pytest.raises(ValueError):
        calcular_temperatura(12000)

# Prueba de Excepción de Tipo (Partición Inválida: String)
def test_error_tipo():
    with pytest.raises(TypeError):
        calcular_temperatura("calorcito")
