# Función que recibe por parámetro cuatro números enteros y va a retornar el mayor de estos, teniendo en cuenta que si hay dos o más mayores, puede retornar cualquiera. 
# Es decir, si tenemos los números 3, 5, 5 y 2, nuestra función puede retornar el primer 5 o el segundo 5 de manera indiferente. 

def mayor_v1(a, b, c, d):
    if (a >= b) and (a >= c) and (a >= d):
        respuesta = a
    elif (b >= a) and (b >= c) and (b >= d):
        respuesta = b
    elif (c >= a) and (c >= b) and (c >= d):
        respuesta = c
    else:
        respuesta = d
    
    return print(respuesta)

mayor_v1(8, 12, 32, 5)