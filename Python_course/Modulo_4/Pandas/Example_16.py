# Construya una función que reciba un DataFrame con información sobre el desempeño de un conjunto de estudiantes en 5 materias y retorne un DataFrame con información sobre los mejores estudiantes.

# El DataFrame que recibe la función tiene 6 columnas: 'nombre', donde aparecen los nombres de los estudiantes, 'matematicas', 'ingles', 'ciencias', 'literatura' y 'arte', en las cuales aparecen las calificaciones de los estudiantes en cada una de esas materias. Las calificaciones son números decimales entre 0 y 5.0.

# La función debe retornar un DataFrame con dos columnas: 'nombre', donde aparecen los nombres de los estudiantes; y 'promedio', donde aparecen los promedios de sus calificaciones redondeados a dos decimales. El DataFrame resultante, debe estar ordenado de mayor a menor promedio y solo deben aparecer los estudiantes cuyo promedio haga parte del mejor 25%.

import pandas as pd

def mejores_estudiantes(estudiantes):
    columnas_materias = ['matematicas', 'ingles', 'ciencias', 'literatura', 'arte']
    # print(notas)

    Suma_notas_estudiantes = estudiantes[columnas_materias].sum(axis = 1)
    promedio = Suma_notas_estudiantes / len(columnas_materias)
    # print(promedio)

    list_nombre_estudiantes = list(estudiantes['nombre'])
    list_promedio_estudiantes = list(promedio)
    # print(list_nombre_estudiantes)
    # print(list_promedio_estudiantes)

    nombre_mas_promedio = {'nombre' : list_nombre_estudiantes, 'promedio' : list_promedio_estudiantes}
    nombre_mas_promedio = pd.DataFrame(nombre_mas_promedio)
    # print(nombre_mas_promedio)

    nombre_mas_promedio_ordenado = nombre_mas_promedio.sort_values(by='promedio', ascending=False)
    # print(nombre_mas_promedio_ordenado)
    mejor_percentil = (len(list_nombre_estudiantes) * 25) / 100
    mejor_percentil = int(mejor_percentil)
    aux_nombre_mas_promedio_ordenado = nombre_mas_promedio_ordenado.iloc[0:mejor_percentil]
    # print(nombre_mas_promedio_ordenado.iloc[0:mejor_percentil])

    list_nombre_estudiantes = list(aux_nombre_mas_promedio_ordenado['nombre'])
    list_promedio_estudiantes = list(aux_nombre_mas_promedio_ordenado['promedio'])
    aux_list_promedio_estudiantes = []

    for i in range(len(list_promedio_estudiantes)):
        list_promedio_estudiantes_round = round(list_promedio_estudiantes[i], 2)
        aux_list_promedio_estudiantes.append(list_promedio_estudiantes_round)

    DataFrame = {'nombre' : list_nombre_estudiantes, 'promedio' : aux_list_promedio_estudiantes}
    DataFrame = pd.DataFrame(DataFrame)

    # print(DataFrame)

    return DataFrame   

e_1 = {'nombre': 'Test_1', 'matematicas': 4.5, 'ingles': 1.5, 'ciencias':2.1, 'literatura': 4.78, 'arte': 2.9}
e_2 = {'nombre': 'Test_2', 'matematicas': 3.5, 'ingles': 2.5, 'ciencias':2.2, 'literatura': 4.78, 'arte': 2.8}
e_3 = {'nombre': 'Test_3', 'matematicas': 2.5, 'ingles': 3.5, 'ciencias':2.3, 'literatura': 4.78, 'arte': 2.7}
e_4 = {'nombre': 'Test_4', 'matematicas': 4.5, 'ingles': 3.5, 'ciencias':2.4, 'literatura': 4.78, 'arte': 2.6}
e_5 = {'nombre': 'Test_5', 'matematicas': 2.5, 'ingles': 4.5, 'ciencias':2.5, 'literatura': 4.78, 'arte': 2.5}
e_6 = {'nombre': 'Test_6', 'matematicas': 4.5, 'ingles': 2.5, 'ciencias':2.6, 'literatura': 4.78, 'arte': 2.4}
e_7 = {'nombre': 'Test_7', 'matematicas': 3.5, 'ingles': 4.8, 'ciencias':2.7, 'literatura': 4.78, 'arte': 2.3}
e_8 = {'nombre': 'Test_8', 'matematicas': 1.5, 'ingles': 2.7, 'ciencias':2.8, 'literatura': 4.78, 'arte': 2.2}
e_9 = {'nombre': 'Test_9', 'matematicas': 2.5, 'ingles': 3.8, 'ciencias':2.8, 'literatura': 4.78, 'arte': 2.1}

estudiantes = [e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9]

df_estudiantes = pd.DataFrame(estudiantes)

print(df_estudiantes)

print(mejores_estudiantes(df_estudiantes))