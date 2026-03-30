def clasificar_calificacion(nota):
    # 1. Validación de Tipo (TypeError)
    if not isinstance(nota, (int, float)):
        raise TypeError("La calificación debe ser un numero")

    # 2. Validación de Rango (ValueError)
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10")

    # 3. Lógica de negocio
    if nota < 6:
        return "Reprobado"
    elif 6 <= nota <= 8:
        return "Aprobado"
    elif 9 <= nota <= 10:
        return "Sobresaliente"
