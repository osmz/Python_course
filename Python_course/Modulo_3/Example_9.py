# Calcular el valor promedio de los números positivos, de una lista de números que contiene tanto positivos como negativos. Recordemos que el promedio se calcula como la sumatoria de los valores del conjunto de datos, en este caso solo los números positivos, dividida entre la cantidad total de datos, que sería el total de números positivos en la lista.

def promedio_lista(numeros):
    sumatoria = 0
    total = 0

    for num in numeros:
        if num > 0:
            sumatoria += num
            total += 1
    
    promedio = sumatoria/total

    return promedio

lista = [4, -1, -4, 5, 1, 6, 10, 17, 31, -14, -61]

print(promedio_lista(lista))
