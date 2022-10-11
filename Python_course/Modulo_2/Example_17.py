# Los estudiantes de un cierto colegio tienen que ver 5 cursos: Matemáticas, Español, Ciencias, Literatura y Arte. La información de cada estudiante se representará usando un diccionario con 6 llaves: "nombre", que tendrá asociado el nombre del estudiante; "matematicas", que tendrá asociada la nota del estudiante en el curso Matemáticas; "español", que tendrá asociada la nota del estudiante en el curso Español; "ciencias", que tendrá asociada la nota del estudiante en el curso Ciencias; "literatura", que tendrá asociada la nota del estudiante en el curso Literatura; y "arte", que tendrá asociada la nota del estudiante en el curso Arte. Las notas son números decimales entre 0 y 5.

# Tu función debe retornar un diccionario con las llaves "matematicas", "español", "ciencias", "literatura" y "arte". Cada llave debe tener asociado el nombre del estudiante que tenga la mejor nota en el curso correspondiente. Si hay dos o más estudiantes que comparten el mejor promedio en algún caso, debes escoger el estudiante que tenga el nombre alfabéticamente menor (el que aparecería primero en un diccionario (de lenguaje hablado y escrito, no el tipo de dato en Python), independientemente de mayúsculas o minúsculas

def mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    dict = {'matematicas': 'None', 'español': 'None', 'ciencias': 'None', 'literatura': 'None', 'arte': 'None'}
    mejores_promedios = {}

    mejor_matematicas = estudiante1
    if (estudiante2['matematicas'] >= mejor_matematicas['matematicas']):
        mejor_matematicas = estudiante2
    if (estudiante3['matematicas'] >= mejor_matematicas['matematicas']):
        mejor_matematicas = estudiante3
    if (estudiante4['matematicas'] >= mejor_matematicas['matematicas']):
        mejor_matematicas = estudiante4
    if (estudiante5['matematicas'] >= mejor_matematicas['matematicas']):
        mejor_matematicas = estudiante5
    if (estudiante1['matematicas'] >= mejor_matematicas['matematicas']):
        mejor_matematicas = estudiante1
    
    if (estudiante2['matematicas'] >= mejor_matematicas['matematicas']):
        mejores_promedios[estudiante2['nombre']] = estudiante2
    if (estudiante3['matematicas'] >= mejor_matematicas['matematicas']):
        mejores_promedios[estudiante3['nombre']] = estudiante3
    if (estudiante4['matematicas'] >= mejor_matematicas['matematicas']):
        mejores_promedios[estudiante4['nombre']] = estudiante4
    if (estudiante5['matematicas'] >= mejor_matematicas['matematicas']):
        mejores_promedios[estudiante5['nombre']] = estudiante5
    if (estudiante1['matematicas'] >= mejor_matematicas['matematicas']):
        mejores_promedios[estudiante1['nombre']] = estudiante1
    
    vector = list()
    for i in range(len(mejores_promedios)):
        print(list(mejores_promedios.keys())[i])
        vector.append(list(mejores_promedios.keys())[i].lower())

    vector.sort()
    print(vector)

    nome = vector[0]

    dict['matematicas'] = nome

    mejores_promedios = {}

    mejor_espanhol = estudiante1
    if (estudiante2['español'] >= mejor_espanhol['español']):
        mejor_espanhol = estudiante2
    if (estudiante3['español'] >= mejor_espanhol['español']):
        mejor_espanhol = estudiante3
    if (estudiante4['español'] >= mejor_espanhol['español']):
        mejor_espanhol = estudiante4
    if (estudiante5['español'] >= mejor_espanhol['español']):
        mejor_espanhol = estudiante5
    if (estudiante1['español'] >= mejor_espanhol['español']):
        mejor_espanhol = estudiante1
    
    if (estudiante2['español'] == mejor_espanhol['español']):
        mejores_promedios[estudiante2['nombre']] = estudiante2
    if (estudiante3['español'] == mejor_espanhol['español']):
        mejores_promedios[estudiante3['nombre']] = estudiante3
    if (estudiante4['español'] == mejor_espanhol['español']):
        mejores_promedios[estudiante4['nombre']] = estudiante4
    if (estudiante5['español'] == mejor_espanhol['español']):
        mejores_promedios[estudiante5['nombre']] = estudiante5
    if (estudiante1['español'] == mejor_espanhol['español']):
        mejores_promedios[estudiante1['nombre']] = estudiante1
    
    vector = list()
    for i in range(len(mejores_promedios)):
        print(list(mejores_promedios.keys())[i])
        vector.append(list(mejores_promedios.keys())[i].lower())

    vector.sort()
    print(vector)

    nome = vector[0]

    dict['español'] = nome

    mejores_promedios = {}
    
    mejor_ciencias = estudiante1
    if (estudiante2['ciencias'] >= mejor_ciencias['ciencias']):
        mejor_ciencias = estudiante2
    if (estudiante3['ciencias'] >= mejor_ciencias['ciencias']):
        mejor_ciencias = estudiante3
    if (estudiante4['ciencias'] >= mejor_ciencias['ciencias']):
        mejor_ciencias = estudiante4
    if (estudiante5['ciencias'] >= mejor_ciencias['ciencias']):
        mejor_ciencias = estudiante5
    if (estudiante1['ciencias'] >= mejor_ciencias['ciencias']):
        mejor_ciencias = estudiante1

    if (estudiante2['ciencias'] == mejor_ciencias['ciencias']):
        mejores_promedios[estudiante2['nombre']] = estudiante2
    if (estudiante3['ciencias'] == mejor_ciencias['ciencias']):
        mejores_promedios[estudiante3['nombre']] = estudiante3
    if (estudiante4['ciencias'] == mejor_ciencias['ciencias']):
        mejores_promedios[estudiante4['nombre']] = estudiante4
    if (estudiante5['ciencias'] == mejor_ciencias['ciencias']):
        mejores_promedios[estudiante5['nombre']] = estudiante5
    if (estudiante1['ciencias'] == mejor_ciencias['ciencias']):
        mejores_promedios[estudiante1['nombre']] = estudiante1
    
    vector = list()
    for i in range(len(mejores_promedios)):
        print(list(mejores_promedios.keys())[i])
        vector.append(list(mejores_promedios.keys())[i].lower())

    vector.sort()
    print(vector)

    nome = vector[0]

    dict['ciencias'] = nome

    mejores_promedios = {}

    mejor_literatura = estudiante1
    if (estudiante2['literatura'] >= mejor_literatura['literatura']):
        mejor_literatura = estudiante2
    if (estudiante3['literatura'] >= mejor_literatura['literatura']):
        mejor_literatura = estudiante3
    if (estudiante4['literatura'] >= mejor_literatura['literatura']):
        mejor_literatura = estudiante4
    if (estudiante5['literatura'] >= mejor_literatura['literatura']):
        mejor_literatura = estudiante5
    if (estudiante1['literatura'] >= mejor_literatura['literatura']):
        mejor_literatura = estudiante1
    
    if (estudiante2['literatura'] >= mejor_literatura['literatura']):
        mejores_promedios[estudiante2['nombre']] = estudiante2
    if (estudiante3['literatura'] >= mejor_literatura['literatura']):
        mejores_promedios[estudiante3['nombre']] = estudiante3
    if (estudiante4['literatura'] >= mejor_literatura['literatura']):
        mejores_promedios[estudiante4['nombre']] = estudiante4
    if (estudiante5['literatura'] >= mejor_literatura['literatura']):
        mejores_promedios[estudiante5['nombre']] = estudiante5
    if (estudiante1['literatura'] >= mejor_literatura['literatura']):
        mejores_promedios[estudiante1['nombre']] = estudiante1
    
    vector = list()
    for i in range(len(mejores_promedios)):
        print(list(mejores_promedios.keys())[i])
        vector.append(list(mejores_promedios.keys())[i].lower())

    vector.sort()
    print(vector)

    nome = vector[0]

    dict['literatura'] = nome

    mejores_promedios = {}

    mejor_arte = estudiante1
    if (estudiante2['arte'] >= mejor_arte['arte']):
        mejor_arte = estudiante2
    if (estudiante3['arte'] >= mejor_arte['arte']):
        mejor_arte = estudiante3
    if (estudiante4['arte'] >= mejor_arte['arte']):
        mejor_arte = estudiante4
    if (estudiante5['arte'] >= mejor_arte['arte']):
        mejor_arte = estudiante5
    if (estudiante1['arte'] >= mejor_arte['arte']):
        mejor_arte = estudiante1
    
    if (estudiante2['arte'] >= mejor_arte['arte']):
        mejores_promedios[estudiante2['nombre']] = estudiante2
    if (estudiante3['arte'] >= mejor_arte['arte']):
        mejores_promedios[estudiante3['nombre']] = estudiante3
    if (estudiante4['arte'] >= mejor_arte['arte']):
        mejores_promedios[estudiante4['nombre']] = estudiante4
    if (estudiante5['arte'] >= mejor_arte['arte']):
        mejores_promedios[estudiante5['nombre']] = estudiante5
    if (estudiante1['arte'] >= mejor_arte['arte']):
        mejores_promedios[estudiante1['nombre']] = estudiante1
    
    vector = list()
    for i in range(len(mejores_promedios)):
        print(list(mejores_promedios.keys())[i])
        vector.append(list(mejores_promedios.keys())[i].lower())

    vector.sort()
    print(vector)

    nome = vector[0]

    dict['arte'] = nome

    return dict

estudiante1 = {'nombre': 'pablo', 'matematicas': 3.4, 'español': 5.0, 'ciencias': 2.9, 'literatura': 4.2, 'arte': 3.2}
estudiante2 = {'nombre': 'andres', 'matematicas': 2.1, 'español': 4.9, 'ciencias': 3.0, 'literatura': 4.1, 'arte': 4.5}
estudiante3 = {'nombre': 'daniela', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 3.7}
estudiante4 = {'nombre': 'maria', 'matematicas': 3.2, 'español': 3.7, 'ciencias': 3.1, 'literatura': 4.7, 'arte': 3.9}
estudiante5 = {'nombre': 'pedro', 'matematicas': 4.7, 'español': 4.2, 'ciencias': 4.7, 'literatura': 2.5, 'arte': 3.2}

print(mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5))

