# Una clase de estudiantes ejemplares ha decidido hacer una vaca para el cumpleaños de su profesor favorito. Para esto, un estudiante recorrerá todo el salón recogiendo el dinero que cada estudiante va a aportar. Tienen dos opciones de regalo: una botella de licor que cuesta 120.000 o un pastel que cuesta 35.000. Además, el estudiante que más dinero ponga, será el que tenga el honor de darle el regalo al profesor. Recree este caso en una función que reciba una matriz que representa al salón y una cadena que indica el regalo. Debe retornar una lista cuya primera posición es un mensaje que indica si el dinero alcanzó para la vaca y las siguientes dos posiciones son las coordenadas del puesto del estudiante que más aportó. 

def hacer_la_vaca(salon, vaca):
    suma = 0
    mayor = 0

    for i in range(0, len(salon)):
        for j in range(0, len(salon[0])):
            suma += salon[i][j]
            if salon[i][j] > mayor:
                mayor = salon[i][j]
                fila = i
                columna = j
    
    if vaca == 'botella' and suma >= 120000:
        regalo = 'Hay Vaca'
    elif vaca == 'pastel' and suma >= 35000:
        regalo = 'Hay Vaca'
    else:
        regalo = 'No Alcanza'

    list = [regalo, fila, columna]

    return list

salon = [[1000,8000,10000], [20000,1000,8000], [8000,5000,1000]]
vaca = 'pastel'
print(hacer_la_vaca(salon, vaca))