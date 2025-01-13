#7. Calculadora básica
#Ejercicio: Crea una calculadora que realice suma, resta, multiplicación y división dependiendo de la 
# opción elegida por el usuario.
#Explicación: Aprenderás a manejar condicionales y entradas de usuario para tomar decisiones.


# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

# Función para realizar la operación correspondiente
def realizar_operacion(opcion, num1, num2):
    if opcion == 1:
        return num1 + num2
    elif opcion == 2:
        return num1 - num2
    elif opcion == 3:
        return num1 * num2
    elif opcion == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Opción no válida"

# Programa principal
def calculadora():
    while True:
        # Mostrar el menú
        mostrar_menu()

        # Solicitar la opción al usuario
        try:
            opcion = int(input("Elige una opción (1/2/3/4): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        # Si el usuario desea salir
        if opcion == 0:
            print("Saliendo de la calculadora...")
            break
        
        # Solicitar los dos números
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue
        
        # Realizar la operación y mostrar el resultado
        resultado = realizar_operacion(opcion, num1, num2)
        print(f"El resultado es: {resultado}")
        print()  # Línea en blanco para mejorar la visualización

# Ejecutar la calculadora
calculadora()
