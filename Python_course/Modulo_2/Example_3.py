# Función que recibe por parámetro un número entero y retorna alguna de los siguientes valores: 
# -1 si es un número negativo
# 0 si es positivo, pero menor a 1000
# 1 si está entre 1000 y 10000 
# 2 si es un número mayor a 10000. 

def rango_numero(x):
    if x < 0:
        respuesta = -1
    elif x < 1000:
        respuesta = 0
    elif x <= 10000:
        respuesta = 1
    else:
        respuesta = 2

    return respuesta
    
print(rango_numero(12000))