def multiplicar(a, b):
    """Multiplica dos numeros y devuelve el resultado."""
    return a * b


def pedir_numero(mensaje):
    """Solicita un numero al usuario y valida la entrada."""
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Entrada invalida. Usa un numero (ej. 3 o 2.5).")


def main():
    print("Calculadora basica - Multiplicacion")
    a = pedir_numero("Ingresa el primer numero: ")
    b = pedir_numero("Ingresa el segundo numero: ")
    resultado = multiplicar(a, b)
    if resultado.is_integer():
        resultado = int(resultado)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
