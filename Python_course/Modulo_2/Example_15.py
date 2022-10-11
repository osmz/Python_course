# Los estudiantes de un cierto colegio tienen que ver 5 cursos: 

# Matemáticas, Español, Ciencias, Literatura y Arte. Usted debe construir una función que reciba la información de 5 estudiantes y calcule quién es el mejor estudiante (el que tenga el mejor promedio). La información de cada estudiante se representará usando un diccionario con 6 llaves: "nombre", que tendrá asociado el nombre del estudiante; "matematicas", que tendrá asociada la nota del estudiante en el curso Matemáticas; "español", que tendrá asociada la nota del estudiante en el curso Español; "ciencias", que tendrá asociada la nota del estudiante en el curso Ciencias; "literatura", que tendrá asociada la nota del estudiante en el curso Literatura; y "arte", que tendrá asociada la nota del estudiante en el curso Arte. Las notas son números decimales entre 0 y 5.

# Su función debe retornar el nombre del estudiante que tenga el mejor promedio. Si hay varios con el mejor promedio, debe aparecer el estudiante que tenga el nombre alfabéticamente menor (independientemente de mayúsculas o minúsculas).

def mejor_del_salon(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    promedio_est1 = round((estudiante1['matematicas'] + estudiante1['español'] + estudiante1['ciencias'] + estudiante1['literatura'] + estudiante1['arte'])/5, 2)
    promedio_est2 = round((estudiante2['matematicas'] + estudiante2['español'] + estudiante2['ciencias'] + estudiante2['literatura'] + estudiante2['arte'])/5, 2)
    promedio_est3 = round((estudiante3['matematicas'] + estudiante3['español'] + estudiante3['ciencias'] + estudiante3['literatura'] + estudiante3['arte'])/5, 2)
    promedio_est4 = round((estudiante4['matematicas'] + estudiante4['español'] + estudiante4['ciencias'] + estudiante4['literatura'] + estudiante4['arte'])/5, 2)
    promedio_est5 = round((estudiante5['matematicas'] + estudiante5['español'] + estudiante5['ciencias'] + estudiante5['literatura'] + estudiante5['arte'])/5, 2)

    mayor_promedio = promedio_est1
    mejores_promedios = {}
    if promedio_est2 >= mayor_promedio:
        mayor_promedio = promedio_est2
        mejores_promedios[estudiante2['nombre']] = promedio_est2
    if promedio_est3 >= mayor_promedio:
        mayor_promedio = promedio_est3
        mejores_promedios[estudiante3['nombre']] = promedio_est3
    if promedio_est4 >= mayor_promedio:
        mayor_promedio = promedio_est4
        mejores_promedios[estudiante4['nombre']] = promedio_est4
    if promedio_est5 >= mayor_promedio:
        mayor_promedio = promedio_est5
        mejores_promedios[estudiante5['nombre']] = promedio_est5
    if promedio_est1 >= mayor_promedio:
        mayor_promedio = promedio_est5
        mejores_promedios[estudiante1['nombre']] = promedio_est1
    
    vector = list()
    for i in range(len(mejores_promedios)):
        print(list(mejores_promedios.keys())[i])
        vector.append(list(mejores_promedios.keys())[i].lower())

    vector.sort()
    print(vector)

    nome = vector[0]
    
    return nome

e_1 = {'nombre': 'Abel', 'matematicas': 4.5, 'español': 3.5, 'ciencias':2.5, 'literatura': 4.78, 'arte': 2.5}
e_2 = {'nombre': 'stiven', 'matematicas': 3.5, 'español': 3.5, 'ciencias':2.5, 'literatura': 4.78, 'arte': 2.5}
e_3 = {'nombre': 'Morales', 'matematicas': 2.5, 'español': 3.5, 'ciencias':2.5, 'literatura': 4.78, 'arte': 2.5}
e_4 = {'nombre': 'Zapata', 'matematicas': 4.5, 'español': 3.5, 'ciencias':2.5, 'literatura': 4.78, 'arte': 2.5}
e_5 = {'nombre': 'Careca', 'matematicas': 1.5, 'español': 3.5, 'ciencias':2.5, 'literatura': 4.78, 'arte': 2.5}

nome = mejor_del_salon(e_1, e_2, e_3, e_4, e_5)
print(nome)