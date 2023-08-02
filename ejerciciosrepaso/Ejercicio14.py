#Escribir una función que calcule la media aritmética de una lista de números

def media_aritmetica(lista):
    suma = sum(lista)
    cantidad_elementos = len(lista)

    if cantidad_elementos == 0:
        return None

    media = suma / cantidad_elementos
    return media
