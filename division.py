def dividir(a, b):
    """
    Retorna la división de a entre b.
    Maneja el error de división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return a / b