# Escriba una función que reciba una cadena de caracteres (str) por parámetro y retorne dicha cadena ordenada alfabéticamente.

# Por ejemplo, si se recibe la palabra "bca", el retorno correcto sería "abc".

# Suponga que las palabras que su función deberá ordenar están compuestas únicamente del alfabeto inglés en minúsculas. La cadena no tiene espacios.

def ordenar_cadena(cadena):
    cadena = sorted(cadena)
    cadena = ''.join(cadena)
    return cadena

print(ordenar_cadena('oscar'))