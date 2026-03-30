import sys

def calcular_temperatura(temp):
    # Validación de tipo (TypeError)
    if not isinstance(temp, (int, float)):
        raise TypeError("El valor debe ser numerico")

    # Validación de rango (ValueError)
    if temp < -273 or temp > 10000:
        raise ValueError("Temperatura fuera de rango")

    # Lógica de clasificación
    if temp <= 15:
        return "Frio"
    elif 16 <= temp <= 25:
        return "Templado"
    else:
        return "Caliente"
