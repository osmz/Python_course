# Crear una función llamada "cantidad_digitos" que nos permita contar la cantidad de dígitos que tiene un número entero. Debemos, además, incluir el programa principal que nos permita pedir el número al usuario y mostrarle la cantidad de dígitos que tiene.

def contar_digitos(numero):
    contador = 0
    terminar = False

    while terminar == False:
        if numero == 0:
            terminar = True
        else:
            contador += 1
            numero //= 10
    
    return contador

num = int(input('Ingrese un numero entero: '))
digitos = contar_digitos(num)
print('La cantidad de dígitos del número es: ', digitos)