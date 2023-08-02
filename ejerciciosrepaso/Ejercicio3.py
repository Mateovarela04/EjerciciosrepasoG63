#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random

lista= [random.randint(1,10) for i in range(10)]

print(lista)