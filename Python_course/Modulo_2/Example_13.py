# Averiguar quién es el estudiante con el mayor promedio, calcular cuántos estudiantes son mujeres y decidir si hay al menos una mujer pila.

def crear_estudiante(nom, cod, gen, carr, prom, ssc):
    dic_estudiante = {'nombre': nom,
                      'codigo': cod,
                      'genero': gen,
                      'carrera': carr,
                      'promedio': prom,
                      'ssc': ssc}
    
    return dic_estudiante

estudiante1 = crear_estudiante('Juan', '1055987485', 'masculino', 'Biologia', 3.7, 0.7)
estudiante2 = crear_estudiante('Ana', '1055987485', 'femenino', 'ciencias politicas', 4.25, 3.5)
estudiante3 = crear_estudiante('Bastien', '1055987485', 'masculino', 'Economia', 3.21, 2.3)
estudiante4 = crear_estudiante('Catalina', '1055987485', 'femenino', 'Arte', 3.8, 4)

print('Los estudiantes son:\n', 'Estudiante 1:\n', estudiante1, '\nEstudiante 2:\n', estudiante2, '\nEstudiante 3:\n', estudiante3, '\nEstudiante 4:\n', estudiante4,)

def mayor_promedio(est1, est2, est3, est4):
    mayor = est1
    if (est2['promedio'] >= mayor['promedio']):
        mayor = est2
    if (est3['promedio'] >= mayor['promedio']):
        mayor = est3
    if (est4['promedio'] >= mayor['promedio']):
        mayor = est4

    return mayor

mejor = mayor_promedio(estudiante1, estudiante2, estudiante3, estudiante4)

print('El estudiante de mayor promedio es: ' + mejor['nombre'] + ' y su promedio es: ' + str(mejor['promedio']))

def cuantas_mujeres(est1, est2, est3, est4):
    cuantas = 0

    if (est1['genero'] == 'femenino'):
        cuantas += 1
    if (est2['genero'] == 'femenino'):
        cuantas += 1
    if (est3['genero'] == 'femenino'):
        cuantas += 1
    if (est4['genero'] == 'femenino'):
        cuantas += 1

    return cuantas

cuantas = cuantas_mujeres(estudiante1, estudiante2, estudiante3, estudiante4)

print('Entre los 4 estudiantes hay: ', cuantas, ' mujeres')

def hay_mujer_pila(est1, est2, est3, est4):
    hay = False

    if (est1['genero'] == 'femenino' and est1['promedio'] >= 4):
        hay = True
    elif (est2['genero'] == 'femenino' and est2['promedio'] >= 4):
        hay = True
    elif (est3['genero'] == 'femenino' and est3['promedio'] >= 4):
        hay = True
    elif (est4['genero'] == 'femenino' and est4['promedio'] >= 4):
        hay = True
    
    return hay

var_hay = hay_mujer_pila(estudiante1, estudiante2, estudiante3, estudiante4)

if (var_hay):
    print('Si hay una mujer pila')
else:
    print('No hay una mujer pila')



