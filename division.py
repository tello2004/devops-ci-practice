def dividir(n1, n2):
    """
    Realiza la división de dos números y maneja la división por cero.
    """
    if n2 == 0:
        return None  # Retorna None para indicar error
    return n1 / n2

if __name__ == "__main__":
    print("--- Calculadora de División ---")
    
    try:
        # Pedimos los datos al usuario desde la consola
        # float() convierte el texto de la consola a número decimal
        a = float(input("Ingresa el primer número (dividendo): "))
        b = float(input("Ingresa el segundo número (divisor): "))
        
        resultado = dividir(a, b)
        
        if resultado is None:
            print("❌ Error: No se puede dividir entre cero.")
        else:
            # Imprimimos el resultado (la 'f' permite poner variables dentro del texto)
            print(f"✅ El resultado de la división es: {resultado}")
            
    except ValueError:
        print("❌ Error: Por favor ingresa solamente números válidos.")