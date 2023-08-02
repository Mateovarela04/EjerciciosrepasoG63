#Crear un programa que calcule la suma de los números en una lista dada.

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista_numeros = [4, 5, 9, 1, 0]

resultado = suma_lista(lista_numeros)

print("La suma de los numeros es:", resultado)