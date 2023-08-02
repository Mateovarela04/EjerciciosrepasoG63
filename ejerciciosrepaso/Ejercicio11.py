#Crear un programa que genere una lista de números pares entre 1 y 100.

#Se crea la lista y se le indica en el for que solo muestre los que cumplan la condicion
lista_pares = [numero for numero in range(1, 101) if numero % 2 == 0]

print(lista_pares)
