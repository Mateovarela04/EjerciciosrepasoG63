#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def encontrar_mayor_y_menor(lista):
    numero_mas_grande = max(lista)
    numero_mas_pequeno = min(lista)
    return numero_mas_grande, numero_mas_pequeno

# Lista de ejemplo
lista_numeros = [5, 2, 9, 1, 7, 3]

# Llamamos a la función
mas_grande,mas_pequeno = encontrar_mayor_y_menor(lista_numeros)

print("El número más grande es:", mas_grande)
print("El número más pequeño es:", mas_pequeno)