#9. Número mayor de tres números
#Ejercicio: Pide tres números al usuario y muestra el mayor de ellos.

#Explicación: Uso de condicionales con if-elif-else para comparar varios valores.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El número mayor es ", num1)
elif num2 > num3 and num2 > num1:
    print("El número mayor es ", num2)
else:
    print("El numero mayor es ", num3)