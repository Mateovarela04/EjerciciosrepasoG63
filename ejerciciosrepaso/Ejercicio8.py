#Crear una función que invierta el orden de los elementos en una lista dada.
def invertir_lista(lista):
    lista.reverse()
    return lista

lista = [4, 67, 78, 3, 0]

#Se llama la función
lista_invertida = invertir_lista(lista)

print("Lista invertida es:", lista_invertida)