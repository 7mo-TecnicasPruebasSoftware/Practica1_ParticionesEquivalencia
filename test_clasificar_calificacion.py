import pytest
from src.clasificar_calificacion import clasificar_calificacion

# --- PARTICIONES VALIDAS ---

def test_reprobado():
    # Particion 1 (nota < 6)
    assert clasificar_calificacion(5.5) == "Reprobado"

def test_aprobado():
    # Particion 2 (6 <= nota < 9)
    assert clasificar_calificacion(7) == "Aprobado"

def test_sobresaliente():
    # Particion 3 (nota >= 9)
    assert clasificar_calificacion(9.5) == "Sobresaliente"

# --- PARTICIONES INVALIDAS ---

def test_error_nota_negativa():
    # Nota fuera de rango inferior (ValueError)
    with pytest.raises(ValueError):
        clasificar_calificacion(-1)

def test_error_nota_excedida():
    # Nota fuera de rango superior (ValueError)
    with pytest.raises(ValueError):
        clasificar_calificacion(11)

def test_error_tipo_dato():
    # Entrada no numerica (TypeError)
    with pytest.raises(TypeError):
        clasificar_calificacion("Excelente")
