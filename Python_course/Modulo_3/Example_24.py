import random
# función que nos retorne la suma de todos los valores de una matriz

def calcular_suma_matriz(matriz):
    suma = 0

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            suma += matriz[i][j]

    return suma

# retornar la suma todos los valores de una fila dada por parámetro

def calcular_suma_fila(matriz, fila):
    suma = 0

    for num_col in range(0, len(matriz[0])):
        suma += matriz[fila][num_col]

    return suma

# De nuevo es calcular una suma, pero esta vez de todos los valores de una determinada columna

def calcular_suma_columna(matriz, columna):
    suma = 0

    for num_fila in range(0, len(matriz)):
        suma += matriz[num_fila][columna]

    return suma

# En éste nos interesa retornar true o false, dependiendo de si en la matriz existe o no al menos un valor negativo. 

def existe_negativo(matriz):
    encontrado = False
    i = 0
    j = 0

    while i < len(matriz) and not encontrado:
        while j < len(matriz[0]) and not encontrado:
            if matriz[i][j] < 0:
                encontrado = True
            j += 1
        i += 1
    
    return encontrado

# retornar la fila con el mayor número de ceros.

def fila_mas_ceros(matriz):
    fila_mas = 0
    max_ceros = 0

    for i in range(0, len(matriz)):
        cant_ceros = 0
        for j in range(0, len(matriz[0])):
            if matriz[i][j] == 0:
                cant_ceros += 1
        
        if cant_ceros > max_ceros:
            max_ceros = cant_ceros
            fila_mas = i
    
    return fila_mas

M = []

for i in range(5):
    fila = []
    for j in range(5):
        numero = random.randint(-2,5)
        fila.append(numero)
    M.append(fila)

print('Matriz')
for fila in M:
    print(fila)

print("\n Resultados: \n")

print('Suma matriz: ' , calcular_suma_matriz(M))
print('Suma fila: ' , calcular_suma_fila(M, 1))
print('Suma columna: ' , calcular_suma_columna(M, 4))
print('Existe negativo: ' , existe_negativo(M))
print('Fila mas ceros: ' , fila_mas_ceros(M))

