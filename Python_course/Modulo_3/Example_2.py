# Crear una función que permita calcular el factorial de un número, que se define como la multiplicación de todos los enteros, desde el uno hasta el número del cual queremos conocer el factorial. Debemos tener en cuenta que cero factorial es igual a uno y que tenemos que incluir un programa principal, en el que solo se acepten enteros positivos. 

def calcular_factorial(n):
    terminar = False
    factorial = 1

    while terminar == False:
        if n == 0:
            terminar =  True
        else:
            factorial *= n
            n -= 1
    
    return factorial

numero = int(input('Ingrese un número entero positivo: '))

while numero < 0:
    print('No se permite números negativos')
    numero = int(input('Ingrese un entero positivo: '))

print(numero, '! es igual a ', calcular_factorial(numero))