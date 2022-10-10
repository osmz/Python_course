# Función que recibe por parámetro tres puntos, es decir, parejas de coordenadas (x,y) de enteros, para un total de seis parámetros y no retorne ("True o False"), dependiendo de si los tres puntos están sobre una misma recta o no, en otras palabras, si son colineales.

#  Antes de poder solucionar el problema, tenemos que entender qué son puntos colineales. Cuando tenemos tres puntos "A" de coordenadas (x1, y1), "B" de coordenadas (x2, y2) y "C" de coordenadas (x3, y3), estos están alineados, si los vectores formados por "AB" y "BC" tienen la misma dirección, cosa que ocurre cuando las pendientes de las rectas que forman dichos vectores son las mismas. En la imagen podemos ver que la pendiente de una recta formada por dos puntos, la calculamos restando las coordenadas "y" de los puntos y dividiendo esto entre la resta de las coordenadas "x" de los puntos.

def son_colineales (x1, y1, x2, y2, x3, y3):
    pendiente_1 = (y2-y1)/(x2-x1)
    pendiente_2 = (y3-y2)/(x3-x2)

    #if pendiente_1 == pendiente_2:
    #    return True
    #else:
    #    return False

    respuesta = False
    if pendiente_1 == pendiente_2:
        respuesta = True

    return respuesta

print(son_colineales(-5,3,-1,-3,1,-6))
print(son_colineales(-5,3,-1,-3,1,6))