# Construya la función calcular_habitantes_por_puesto que calcule la cantidad de habitantes que hay en un país, por cada estudiante inscrito en una universidad de ese país y clasificada en el ranking TIMES.

# La función recibe dos DataFrames. El primero tiene la información sobre la población de cada país organizada en tres columnas: 'Pais', 'Poblacion' y 'Edad_mediana'. El segundo tiene la información sobre universidades organizada en tres columnas: 'country', con el nombre del país; 'university_name', con el nombre de una universidad del ranking; y 'num_students', con el número de estudiantes inscritos en esa universidad.

# Su función debe retornar un DataFrame con las siguientes condiciones:

# Una columna llamada 'Pais' con el nombre de los países.

# Una columna llamada 'habitantes_por_puesto'. 

# En esta última columna aparecerá la cantidad de habitantes de cada país, dividida por la cantidad total de estudiantes que hay en las universidades del país que aparecen en el ranking TIMES. Por ejemplo, si la población de Australia es de 25 millones de personas y hay 31 universidades que en total atienden a 740.000 estudiantes, entonces la cantidad de 'habitantes_por_puesto' será 33.8 (el número debe redondearse a 1 cifra decimal). Además, el DataFrame resultante debe estar ordenado de menor a mayor de acuerdo con la cantidad de 'habitantes_por_puesto'.

# Nota: para ordenar los resultados no tenga en cuenta las aproximaciones.

import pandas as pd

def aproximar(numero):
    return round(numero, 1)

def calcular_habitantes_por_puesto(poblacion, universidades):
    cant_estudiantes = universidades.groupby('country')

    country_cant_estudiantes = []
    for name, group in cant_estudiantes:
        aux_country_cant_estudiantes = name
        country_cant_estudiantes.append(aux_country_cant_estudiantes)
        print(name, len(group))

    #print(cant_estudiantes.get_group('Colombia').sum())
    #print(cant_estudiantes.get_group('España').sum())

    sum_cant_estudiantes = cant_estudiantes['num_students'].sum()
    sum_cant_estudiantes_1 = []
    for i in range(len(sum_cant_estudiantes)):
        aux_sum_cant_estudiantes_1 = sum_cant_estudiantes[i]
        sum_cant_estudiantes_1.append(aux_sum_cant_estudiantes_1)

    DataFrame_1 = {'pais_country' : country_cant_estudiantes, 'num_students' : sum_cant_estudiantes_1}
    DataFrame_1 = pd.DataFrame(DataFrame_1)

    mezcla = pd.merge(poblacion, DataFrame_1, left_on = 'Pais', right_on= 'pais_country')

    Pais = mezcla['Pais']
    Poblacion = mezcla['Poblacion']
    habitante_por_puesto = mezcla['num_students']
    promedio_habitante_por_puesto = []
    for i in range(len(Pais)):
        aux_habitante_por_puesto = Poblacion[i] / habitante_por_puesto[i]
        promedio_habitante_por_puesto.append(aux_habitante_por_puesto)

    DataFrame = {'Pais' : Pais, 'habitantes_por_puesto' : promedio_habitante_por_puesto}
    DataFrame = pd.DataFrame(DataFrame)

    DataFrame = DataFrame.sort_values(by='habitantes_por_puesto', ascending=True)
    list_nombre_pais = list(DataFrame['Pais'])
    list_promedio_habitante = list(DataFrame['habitantes_por_puesto'])

    list_promedio_habitante_1 = []
    for i in range(len(list_promedio_habitante)):
        aux_list_promedio_habitante_round = round(list_promedio_habitante[i], 1)
        list_promedio_habitante_1.append(aux_list_promedio_habitante_round)

    DataFrame = {'Pais' : list_nombre_pais, 'habitantes_por_puesto' : list_promedio_habitante_1}
    DataFrame = pd.DataFrame(DataFrame)
    
    return DataFrame

p_1 = {'Pais': 'Colombia', 'Poblacion': 50000000, 'Edad_media': 40}
p_2 = {'Pais': 'España', 'Poblacion': 25000000, 'Edad_media': 40}
p_3 = {'Pais': 'Francia', 'Poblacion': 50000000, 'Edad_media': 40}
poblacion = [p_1, p_2, p_3]
poblacion = pd.DataFrame(poblacion)
print(poblacion)

u_1 = {'country': 'Colombia', 'num_students': 5000, 'university_name': 'UAM'}
u_2 = {'country': 'España', 'num_students': 740000, 'university_name': 'Andes'}
u_3 = {'country': 'Colombia', 'num_students': 1000, 'university_name': 'Militar'}
universidades = [u_1, u_2, u_3]
universidades = pd.DataFrame(universidades)
print(universidades)

print(' ')
print(' ')

print(calcular_habitantes_por_puesto(poblacion, universidades))