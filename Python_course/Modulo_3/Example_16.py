# Una clase de la Universidad de los Andes tiene las siguientes reglas con respecto a las aproximaciones de las notas finales.  

# Si la nota es mayor o igual a 4.5, la nota se aproxima a 5.0.
 
# Si la nota es mayor o igual a 3.5 y menor a 4.5, la nota se aproxima a 4.0.
 
# Si la nota es mayor o igual a 2.5 y menor a 3.5, la nota se aproxima a 3.0.
 
# De lo contrario, la nota asignada será 1.5.  
 
# Teniendo una lista de diccionarios en donde cada uno corresponde a un estudiante y que tiene como llaves "nombre" y "nota" (sin aproximar), retorne una lista con todos los diccionarios actualizados con sus notas después de aproximación.
 
# Cada uno de los diccionarios retornados tiene las llaves "nombre" y "nota"(aproximada).
 
# Se garantiza que la lista tiene al menos un diccionario.  

def calcular_definitivas(estudiantes):
    notas = []
    
    for estudiante in estudiantes:
        nota = estudiante['nota']
        print(nota)

        if nota >= 4.5:
            nota = 5.0
        elif nota>= 3.5 and nota < 4.5:
            nota = 4.0
        elif nota >= 2.5 and nota < 3.5:
            nota = 3.0
        else:
            nota = 1.5

        dic_notas = {'nombre':estudiante['nombre'], 'nota': nota}
        notas.append(dic_notas)

    return notas
    

estudiantes = [{'nombre':'Carlos', 'nota':4.5},
                {'nombre':'Andres', 'nota':3.75},
                {'nombre':'Mauricio', 'nota':2.85},
                {'nombre':'Julio', 'nota':2.4}]

print(calcular_definitivas(estudiantes))