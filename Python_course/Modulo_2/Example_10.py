# Pedro es un estudiante inteligente pero desinteresado por algunas de sus materias. A Pedro le gustan las clases en las que aprende programación, matemática, filosofía y literatura. Por lo anterior, cualquier materia que lleve en su título alguna de estas palabras, será de su agrado.

# Pedro está planeando su horario, pero ha puesto a su asistente digital a que le dé posibles conjuntos de tres materias para inscribir en su semestre. Él quiere saber, dados los títulos de las tres materias, cuántas de estas son de su agrado. Se sabe que los nombres de las materias irán sin acentos y en minúsculas cuando sean recibidos por parámetro en la función.

def conteo_de_materias(nombre_materia_1, nombre_materia_2, nombre_materia_3):
    cont = 0
    if 'programacion' in nombre_materia_1:
        cont += 1
    if 'programacion' in nombre_materia_2:
        cont += 1
    if 'programacion' in nombre_materia_3:
        cont += 1
    if 'matematica' in nombre_materia_1:
        cont += 1
    if 'matematica' in nombre_materia_2:
        cont += 1
    if 'matematica' in nombre_materia_3:
        cont += 1
    if 'filosofia' in nombre_materia_1:
        cont += 1
    if  'filosofia' in nombre_materia_2:
        cont += 1
    if 'filosofia' in nombre_materia_3:
        cont += 1
    if 'literatura' in nombre_materia_1:
        cont += 1
    if 'literatura' in nombre_materia_2:
        cont += 1
    if 'literatura' in nombre_materia_3:
        cont += 1
    
    return cont

print(conteo_de_materias('matematicas', 'filosofia', 'sociales'))
    