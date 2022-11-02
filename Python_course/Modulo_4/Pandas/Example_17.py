# Un hacker alteró los resultados de los partidos de un torneo suramericano de fútbol y ahora la CONMEBOL tiene que hacer algo para corregir la información averiada. Escriba una función que reciba la información con problemas en un DataFrame y retornará otro DataFrame con la información corregida.

# El DataFrame que se recibe tiene siguientes columnas: 

# 'local': el nombre del equipo local en cada partido.

# 'visitante': el nombre del equipo visitante en cada partido.

# 'goles_local': la cantidad de goles que anotó el equipo local en cada partido.

# 'goles_visitante': la cantidad de goles que anotó el equipo visitante en cada partido.

# 'resultado': el resultado del partido, es decir el nombre del equipo ganador o la cadena 'empate' en caso de que hayan anotado la misma cantidad de goles.

# Durante el análisis del ataque informático, la CONMEBOL descubrió que el hacker sólo realizó 3 tipos de daños:

# Alteró la columna 'resultado' de forma aleatoria.

# Introdujo valores nulos en la cantidad de goles, tanto de los equipos locales como de los visitantes.

# Alteró los nombres de los equipos.

# Según lo que decidió la CONMEBOL, la función debe corregir estos errores de la siguiente manera:

# En la columna 'resultado' debe quedar el resultado correcto del partido (el nombre del equipo ganador o la cadena 'empate').

# Debe remplazar las cantidades de goles por 0 cuando se encuentren valores nulos.

# Debe eliminar los partidos en los cuales aparezca que un equipo jugó contra él mismo.

# Los valores del DataFrame resultante deben tener el mismo orden en el que se recibieron originalmente

import pandas as pd

def depurar_partidos(partidos):
    local = partidos['local']
    visitante = partidos['visitante']
    goles_local = partidos['goles_local']
    goles_visitante = partidos['goles_visitante']
    resultado = partidos['resultado']

    goles_local = goles_local.fillna(0)
    goles_visitante = goles_visitante.fillna(0)

    resultado_1 = resultado.copy()
    for i in range(len(goles_local)):
        if goles_local[i] < goles_visitante[i]:
            resultado_1[i] = visitante[i]
        elif goles_local[i] > goles_visitante[i]:
            resultado_1[i] = local[i]
        else:
            resultado_1[i] = 'empate'
    
    repetido = []
    for i in range(len(local)):
        if local[i] == visitante[i]:
            repetido.append(i)
    
    DataFrame = {'local': local, 'visitante': visitante, 'goles_local': goles_local, 'goles_visitante': goles_visitante, 'resultado': resultado_1}
    DataFrame = pd.DataFrame(DataFrame)

    DataFrame = DataFrame.drop(repetido, axis = 0)

    return DataFrame

p_1 = {'local': 'Carlos', 'visitante': 'Carlos', 'goles_local': 4, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_2 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': 1, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_3 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': 4, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_4 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': None, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_5 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': 1, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_6 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': 4, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_7 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': 4, 'goles_visitante': 2, 'resultado': 'Test_1'}
p_8 = {'local': 'Test_1', 'visitante': 'Prueba_1', 'goles_local': None, 'goles_visitante': 0, 'resultado': 'Test_1'}
p_9 = {'local': 'Test_1', 'visitante': 'Test_1', 'goles_local': 4, 'goles_visitante': 2, 'resultado': 'Test_1'}

partidos = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9]

partidos = pd.DataFrame(partidos)

print(partidos)
print(' ')
print(depurar_partidos(partidos))

# numpy.Nan pandas.NaT None