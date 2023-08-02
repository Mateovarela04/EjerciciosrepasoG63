#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división

num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa otro numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Antes de hacer la division se Verifica si el segundo número no es 0 antes de hacer la división

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir por 0"

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
