# Función que nos retorna la cadena con mayor número de a entre cuatro cadenas de caracteres. 
#
# Tenemos que tener presente que debemos contar todas las letras a independiente de si están en mayúscula o minúscula y que en caso de que varias cadenas tengan la cantidad mayor de a, debemos retornar la primera de estas.

def mas_a(c1, c2, c3, c4):
    letra = 'a'
    cadena_mas = c1
    cantidad_mas = c1.lower().count(letra)

    if c2.lower().count(letra) > cantidad_mas:
        cadena_mas = c2
        cantidad_mas = c2.lower().count(letra)
    if c3.lower().count(letra) > cantidad_mas:
        cadena_mas = c3
        cantidad_mas = c3.lower().count(letra)
    if c4.lower().count(letra) > cantidad_mas:
        cadena_mas = c4
        cantidad_mas = c4.lower().count(letra)
    
    return cadena_mas

print(mas_a('Acampar', 'fresa', 'carro', 'manzana'))