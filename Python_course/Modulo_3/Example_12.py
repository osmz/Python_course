# Función que encuentra el mayor número en una lista de enteros positivos.

# En caso de que la lista esté vacía, se debe retornar -1.

def encontrar_mayor(entrada):
    if len(entrada) > 0:
        salida = max(entrada)
    else:
        salida = -1

    return salida

print(encontrar_mayor([])) 