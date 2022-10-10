# Funcion para contar la cantidad de ocurrencias o veces que aparece cada uno de los dígitos del cero al nueve dentro de un numero de diez cifras.

# Version 1

#def contar(num, diccionario):
#    digito = num % 10
#
#    if digito in diccionario:
#        diccionario[digito] += 1
#    else:
#        diccionario[digito] = 1
#    
#    return num // 10
#
#numero = int(input('Ingrese el número de 10 cifras: '))
#conteo = {}
#
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#numero = contar(numero, conteo)
#
#print(conteo)

# Version 2

def contar(num, diccionario):
    digito = num % 10

    diccionario[digito] = diccionario.get(digito, 0) + 1
    
    return num // 10

numero = int(input('Ingrese el número de 10 cifras: '))
conteo = {}

numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)

print(conteo)

