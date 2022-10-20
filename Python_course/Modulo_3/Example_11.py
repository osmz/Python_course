# Escriba una función que reciba una lista y un número entero a buscar, y que retorne un entero que indique el índice en que se encuentra este elemento.

# En caso de que el elemento se encuentre más de una vez dentro de la lista, debe retornar la primera posición en que lo encuentre.

# En caso de no encontrar el número, retorne -1.

def buscar_elemento(entrada, buscado):
    if buscado in entrada:
        salida = entrada.index(buscado)
    else:
        salida = -1

    return salida

print(buscar_elemento([1,2,3,4,5,6,7], 8))