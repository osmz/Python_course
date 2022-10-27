# Recopilamos los registros de los vuelos que ocurrieron durante un día entre aeropuertos ubicados en Estados Unidos y los organizamos en un diccionario de diccionarios. Ahora queremos que nos ayudes a identificar si hay aeropuertos a los cuales hayan llegado vuelos durante ese día, pero no hayan salido vuelos.

# El parámetro vuelos de la función es un diccionario de diccionarios con la información de los vuelos.

# Las llaves en este diccionario son el código de cada vuelo.

# Los valores en este diccionario son diccionarios con la información de un vuelo, organizado de acuerdo con las siguientes llaves:

# aerolínea, que corresponde al nombre de la aerolínea

# origen, que corresponde al código de aeropuerto de origen

# destino, que corresponde al aeropuerto destino del vuelo

# distancia, que corresponde a la distancia entre el origen y el destino

# retraso, que corresponde a la cantidad de minutos de retraso que tuvo el vuelo

# duracion, que corresponde a la duración planeada del vuelo en minutos

# salida, que corresponde a un entero que representa la hora de salida.

# La hora de salida se representa usando la hora en formato 24 horas multiplicada por 100 más la cantidad de minutos (por ejemplo, las 2007 indica que el vuelo salió a las 8:07 pm).

def listar_aeropuetos_sin_salida(vuelos):
    no_salieron = []

    for codigo in vuelos:
        info_vuelo = vuelos[codigo]
        if info_vuelo['salida'] == 0:
            no_salieron.append(codigo)
    
    return no_salieron
