import os
import time

# --- IMPORTACIÓN DE TUS FUNCIONES ---
# Asegúrate de que los nombres de archivo (sin .py) coincidan con el primer parámetro
# y que el nombre de la función coincida con el segundo.
try:
    from suma import sumar
    from resta import restar
    from multiplicacion import multiplicar
    from division import dividir
    
    # from division import dividir  <-- Agrega tus otros archivos aquí
except ImportError as e:
    print(f"Error crítico: Falta un archivo de función o la función no existe. Detalles: {e}")
    exit()

def limpiar_pantalla():
    # Detecta el sistema operativo para limpiar la consola correctamente
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("===================================")
    print("   CALCULADORA DE TERMINAL MODULAR")
    print("===================================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("===================================")

def obtener_numeros():
    """Helper para pedir inputs y evitar repetir código"""
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a, b
    except ValueError:
        print("Error: Por favor ingresa solo números válidos.")
        return None, None

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Saliendo del programa...")
            break

        # Lógica de selección
        if opcion in ['1', '2', '3', '4']:
            num1, num2 = obtener_numeros()
            
            if num1 is not None:
                resultado = None
                
                if opcion == '1':
                    # Aquí llamas a tu función externa
                    resultado = sumar(num1, num2)
                elif opcion == '2':
                    resultado = restar(num1, num2)
                elif opcion == '3':
                    resultado = multiplicar(num1, num2)
                elif opcion == '4':
                    resultado = dividir(num1, num2) 
                    pass 

                print(f"\n>>> El resultado es: {resultado}")
        else:
            print("\nOpción no válida, intenta de nuevo.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()