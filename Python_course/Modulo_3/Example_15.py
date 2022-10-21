# La secretaria de una agencia de vuelos necesita poder informar a los clientes la hora de llegada de sus vuelos. Para poder determinar esto, conoce la hora de salida de los vuelos en horas, minutos y segundos, y la duración de cada vuelo, también en horas, minutos y segundos. Como ejemplo, podemos tomar un vuelo que parte a las 11, 48, con 10 segundos, con una duración de 2 horas, 11 minutos y 58 segundos. Así que estará llegando a las 14 horas, 0 minutos, 8 segundos. Podemos suponer que todos los vuelos llegan el mismo día en que parten. Debemos escribir entonces una función que reciba una lista de diccionarios donde cada uno contiene la información de un vuelo que es hora de partida y duración, y retorne otra lista de diccionarios con la hora de llegada de cada uno.

def calcular_hora_llegada(hora_salida, minutos_salida, seg_salida, horas_duracion, minutos_duracion, seg_duracion):
    hora = 0
    minutos = 0
    segundos = 0

    segundos = seg_salida + seg_duracion

    if segundos >= 60:
        segundos -= 60
        minutos += 1
    
    suma_minutos = minutos_salida + minutos_duracion

    minutos += suma_minutos

    if minutos >= 60:
        minutos -= 60
        hora += 1

    suma_horas = hora_salida + horas_duracion
    hora += suma_horas

    return '{0:0>2d}:{1:0>2d}:{2:0>2d}:'.format(hora, minutos, segundos)

print('Calcular hora llegada')
print(calcular_hora_llegada(11,48,10,2,11,58))

def hora_llegada_vuelos(info_vuelos):
    llegadas = []

    for vuelo in info_vuelos:
        salida = vuelo['tiempo_salida']
        duracion = vuelo['duracion']

        partes_salida = salida.split(':')
        hora_salida = int(partes_salida[0])
        minutos_salida = int(partes_salida[1])
        segundos_salida = int(partes_salida[2])
        partes_duracion = duracion.split(':')
        hora_duracion = int(partes_duracion[0])
        minutos_duracion = int(partes_duracion[1])
        segundos_duracion = int(partes_duracion[2])

        tiempo_llegada = calcular_hora_llegada(hora_salida, minutos_salida, segundos_salida, hora_duracion, minutos_duracion, segundos_duracion)

        dic_llegada = {'tiempo_llegada':tiempo_llegada}
        llegadas.append(dic_llegada)
    
    return llegadas

vuelos = [{'tiempo_salida':'08:11:45', 'duracion':'2:54:20'},
        {'tiempo_salida':'11:48:10', 'duracion':'2:11:58'},
        {'tiempo_salida':'12:00:10', 'duracion':'0:50:15'},
        {'tiempo_salida':'14:55:10', 'duracion':'3:20:00'},
        {'tiempo_salida':'17:15:20', 'duracion':'4:05:11'}]

print('Hora llegada vuelos')
print(hora_llegada_vuelos(vuelos))

# Ahora nos piden escribir una función que retorne el vuelo que llega más tarde. Veamos de nuevo qué estrategia seguir para la solución, para luego proceder al código. Lo primero será poder comparar dos horas de llegada. Para esto, necesitaremos otra función. Y empezamos comparando las horas de los dos tiempos. Si alguna es mayor que la otra, si las horas serán iguales, debemos comparar los minutos. Y si alguna es mayor, you tenemos nuestra respuesta. De nuevo, si los minutos serán iguales, toca comparar los segundos, y si alguna es mayor sabremos cuál de los dos tiempos es mayor. En caso de ser iguales, también significaría que ambos tiempos son exactamente iguales. La función nos retornará entonces 0 si ambos tiempos comparados son iguales, 1 si el primero es mayor al segundo, y menos 1 en caso contrario. Finalmente, la solución a encontrar el vuelo que llega más tarde consistirá en recorrer la lista de vuelos, comparando las horas de llegada que obtenemos al invocar la función que hicimos como solución al primer problema, para buscar el mayor usando el algoritmo de búsqueda secuencial que hemos visto en el curso para hallar el mayor.

def comparar_tiempos(tiempo_1, tiempo_2):
    partes_1 = tiempo_1.split(':')
    partes_2 = tiempo_2.split(':')

    hora_1 = int(partes_1[0])
    minutos_1 = int(partes_1[1])
    segundos_1 = int(partes_1[2])

    hora_2 = int(partes_2[0])
    minutos_2 = int(partes_2[1])
    segundos_2 = int(partes_2[2])

    comparar = 0

    if hora_1 > hora_2:
        comparar = 1
    elif hora_1 < hora_2:
        comparar = -1
    else:
        if minutos_1 > minutos_2:
            comparar = 1
        elif minutos_1 < minutos_2:
            comparar = -1
        else:
            if segundos_1 > segundos_2:
                comparar = 1
            elif segundos_1 < segundos_2:
                comparar = -1
    
    return comparar

def vuelo_llega_mas_tarde(vuelos):
    llegadas = hora_llegada_vuelos(vuelos)

    pos_mas_tarde = 0
    llegada_mas_tarde = llegadas[0]['tiempo_llegada']

    for i in range(0, len(llegadas)):
        tiempo = llegadas[i]['tiempo_llegada']

        if comparar_tiempos(tiempo, llegada_mas_tarde):
            pos_mas_tarde = i
            llegada_mas_tarde = tiempo
    
    return vuelos[pos_mas_tarde]

vuelos = [{'tiempo_salida':'08:11:45', 'duracion':'2:54:20'},
        {'tiempo_salida':'11:48:10', 'duracion':'2:11:58'},
        {'tiempo_salida':'12:00:10', 'duracion':'0:50:15'},
        {'tiempo_salida':'14:55:10', 'duracion':'3:20:00'},
        {'tiempo_salida':'17:15:20', 'duracion':'4:05:11'}]

print('Vuelo llega mas tarde')
print(vuelo_llega_mas_tarde(vuelos))