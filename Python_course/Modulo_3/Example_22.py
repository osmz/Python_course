# Como parte de una iniciativa de analítica sobre el desempeño de los estudiantes para identificar las dificultades que tienen en un curso, se recopilaron las notas que obtuvieron en diferentes tareas. Ahora, queremos analizarlas con un pequeño programa que usted tendrá que construir.

# La información obtenida está organizada en un diccionario donde las llaves son los nombres de los estudiantes (cadenas de caracteres) y los valores son diccionarios.

# En estos diccionarios "internos", las llaves son los nombres de las tareas y los valores son las notas obtenidas por el estudiante para esa tarea (un número entero entre 0 y 100).

# Es decir, si el único estudiante en la muestra se llama "Roberto" y ha realizado dos tareas ("Tarea 1" y "Tarea 2" con notas de 80 y 90 respectivamente), el diccionario de diccionarios con esta información se vería en Python de la siguiente forma: {"Roberto": {"Tarea 1": 80, "Tarea 2" : 90}}.

# Tenga cuidado: no todos los estudiantes resolvieron todas las tareas.

# Usted debe construir una función que, dados los resultados de los estudiantes, calcule las siguientes estadísticas para una tarea dada su nombre: la mayor nota obtenida, el nombre del estudiante que obtuvo la mejor nota, la menor nota obtenida, el nombre del estudiante que obtuvo la peor nota, el promedio de las notas de los estudiantes, la cantidad de estudiantes que recibieron una nota y la suma de las notas obtenidas por los estudiantes.

# La función debe retornar un diccionario con las siguientes llaves: "mayor", "mejor", "menor", "peor", "promedio", "cantidad" y "total".

def calcular_estadisticas_tarea(estudiantes_tareas, nombre_tarea):
    nombre_estudiante = []
    nota = []

    for estudiante, asignacion in estudiantes_tareas.items():
        if nombre_tarea in asignacion:
            nombre_estudiante.append(estudiante)
            nota.append(asignacion[nombre_tarea])
            mayor = max(nota)
            menor = min(nota)

            if asignacion[nombre_tarea] == mayor:
                mejor = estudiante
            
            if asignacion[nombre_tarea] == menor:
                peor = estudiante
            
            cantidad = len(nota)

            total = sum(nota)
            
            promedio = total/cantidad
    
    dict = {'mayor': mayor, 'mejor': mejor, 'menor': menor, 'peor': peor, 'promedio': promedio, 'cantidad': cantidad, 'total': total}
   
    return dict