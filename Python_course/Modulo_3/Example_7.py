# Escriba una función que cuente la cantidad de caracteres diferentes que aparecen más de una vez en una cadena.

# Suponga que todas las cadenas se componen únicamente de letras minúsculas del alfabeto en inglés.

def contar_caracteres_repetidos(cadena):
    contador = 0
    letra = set(cadena)
    print(letra)

    for i in letra:
        if cadena.count(i)>1:
            contador +=1

    return contador

print(contar_caracteres_repetidos('abcdefg'))