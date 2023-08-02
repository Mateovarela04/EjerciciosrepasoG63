#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
def es_palindromo(cadena):
    # Eliminamos los espacios en blanco y convierte todo en minusculas
    cadena = cadena.replace(" ", "").lower()

    # Comparamos la cadena original con su versión invertida
    return cadena == cadena[::-1]

# Pedimos al usuario que ingrese una cadena de texto
cadena_texto = input("Ingresa una cadena de texto: ")

# Llamamos a la función y verificamos si es un palíndromo
if es_palindromo(cadena_texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena NO es un palíndromo.")
