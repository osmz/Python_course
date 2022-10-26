# Andrés es un profesor que tiene la teoría de que hay filas del salón que tienen mejor promedio que otras.

# Para comprobarlo, ha decidido crear una función que calcule el promedio de la nota de una fila. La función recibe como parámetros una matriz, un número de fila y retorna el promedio de la fila redondeado a dos decimales.

# Cuidado: un 0 en la matriz no significa que el estudiante haya sacado 0, sino que no hay ningún estudiante en dicha silla.

# Tenga muy en cuenta que para Andrés la primera fila es la número 1. Si se pide un número de fila que no tenga sentido, su función debe retornar -1. Si la fila no tiene estudiantes, su función debe retornar 0. 

def promedio_fila(matriz, fila):
    suma = 0
    suma2 = 0
    cant1 = 0
    cant2 = 0

    if fila >= 1 and fila <= len(matriz):

        for num_col in range(0, len(matriz[fila - 1])):
            if matriz[fila-1][num_col] != 0:
                suma += matriz[fila-1][num_col]
                cant1 += 1
            else:
                suma2 += matriz[fila-1][num_col]
                cant2 += 1
        
        if suma2 == 0 and cant2 == len(matriz[fila - 1]):
            print('3')
            print(matriz[fila - 1])
            print(len(matriz))
            promedio = 0
        else:
            if cant1 == len(matriz[fila - 1]):
                print('1')
                print(matriz[fila - 1])
                print(len(matriz))
                promedio = suma/len(matriz[fila - 1])
                promedio = round(promedio,2)
            else:
                print('2')
                print(matriz[fila - 1])
                promedio = suma/(len(matriz[fila - 1]) - cant2)
                promedio = round(promedio,2)      
    else:
        promedio = -1

    return promedio

matriz = [[3.25, 4.53, 4.3, 3.61, 2.75],
        [0, 0],
        [4.3], 
        [4.59, 2.75, 3.74, 1, 2.79, 2], 
        [4.3]]
fila = 5
print(promedio_fila(matriz, fila))