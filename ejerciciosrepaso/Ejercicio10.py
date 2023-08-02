#Escribir una función que calcule el factorial de un número dado.

numero = int(input("Ingrese un número entero y positivo: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")
