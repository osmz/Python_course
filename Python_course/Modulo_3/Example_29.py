# En este ejercicio deberás identificar la letra más común (o moda) en una cadena recibida por parámetro. Crea una función que reciba una cadena (str) que será analizada, y que retorne otra cadena (str) que contenga la letra más común en la cadena inicial.

# Para tu facilidad, las cadenas que recibirás solo contendrán letras mayúsculas y no tendrán tildes o acentos. No obstante, estas pueden tener espacios, puntos y comas.

# En caso de que haya 2 letras con la misma cantidad de apariciones, debes retornar la que sea alfabéticamente posterior.

def letra_mas_comun(cadena):
    #reemplazamos espacios, comas y puntos por nada así no molestan
    cadena = cadena.replace(" ","").replace(",","").replace(".","")
 
    dic = {}
    #llenamos un diccionario con las letras y sus apariciones
    for letra in cadena:
        ocurrencias = cadena.count(letra)
        dic[letra] = ocurrencias

    #obtenemos el valor mayor del diccionario
    mayor = dic[max(dic, key = dic.get)]

    #creamos una lista con tuplas de todas las letras iguales al valor mayor
    lista = [(key,value) for key,value in dic.items() if value == mayor]

    #devolvemos el primer elemento de la última tupla
    letra = sorted(lista)[-1][0]

    return letra

cadena = 'MIMAMAMEMIMAOOOOOO'
print(letra_mas_comun(cadena))