# Debemos crear una función llamada buscar_estudiante que recibe los cuatro diccionarios que representan los estudiantes y un string que corresponde al nombre de un estudiante. 

# La función debe retornar el diccionario del estudiante cuyo nombre es idéntico al dado por el parámetro o None, en caso de que ninguno de los estudiantes tenga dicho nombre.

def buscar_estudiante(est1, est2, est3, est4, nom):
    buscado = None

    if est1['nombre'] == nom:
        buscado = est1
    elif est2['nombre'] == nom:
        buscado = est2
    elif est3['nombre'] == nom:
        buscado = est3
    elif est4['nombre'] == nom:
        buscado = est4
    
    return buscado

e_1 = {'nombre': 'Lina', 'codigo': '2020101234', 'genero':'femenino', 'carrera':'Sistemas', 'promedio': 4.78, 'ssc':2}
e_2 = {'nombre': 'Laura', 'codigo': '2020101234', 'genero':'femenino', 'carrera':'Civil', 'promedio': 4.21, 'ssc':2}
e_3 = {'nombre': 'Felipe', 'codigo': '2020101234', 'genero':'masculino', 'carrera':'Sistemas', 'promedio': 4.9, 'ssc':2}
e_4 = {'nombre': 'CarlosLina', 'codigo': '2020101234', 'genero':'masculino', 'carrera':'Economia', 'promedio': 3.89, 'ssc':2}

nombre = input('Ingrese el nombre del estudiante a buscar: ')

est_buscado = buscar_estudiante(e_1, e_2, e_3, e_4, nombre)

if est_buscado is None:
    print('El estudiante no existe')
else:
    print('El estudiante existe y su codigo es ' + est_buscado['codigo'])

#  Ahora se pide crear la función avanzar_trimestre, que debe modificar los diccionarios de los cuatro estudiantes para avanzar el semestre según créditos en uno sin dar retorno alguno. 

def avanzar_semestre(est1, est2, est3, est4):
    est1['ssc'] += 1
    est2['ssc'] += 1
    est3['ssc'] += 1
    est4['ssc'] += 1

e_1 = {'nombre': 'Lina', 'codigo': '2020101234', 'genero':'femenino', 'carrera':'Sistemas', 'promedio': 4.78, 'ssc':4}
e_2 = {'nombre': 'Laura', 'codigo': '2020101234', 'genero':'femenino', 'carrera':'Civil', 'promedio': 3.21, 'ssc':1}
e_3 = {'nombre': 'Felipe', 'codigo': '2020101234', 'genero':'masculino', 'carrera':'Sistemas', 'promedio': 4.9, 'ssc':2}
e_4 = {'nombre': 'CarlosLina', 'codigo': '2020101234', 'genero':'masculino', 'carrera':'Economia', 'promedio': 3.89, 'ssc':3}

print('Semestre estudainte 1: ', e_1['ssc'])
print('Semestre estudainte 2: ', e_2['ssc'])
print('Semestre estudainte 3: ', e_3['ssc'])
print('Semestre estudainte 4: ', e_4['ssc'])

avanzar_semestre(e_1, e_2, e_3, e_4)

print('Nuevo semestre estudiante 1: ', e_1['ssc'])
print('Nuevo semestre estudiante 2: ', e_2['ssc'])
print('Nuevo semestre estudiante 3: ', e_3['ssc'])
print('Nuevo semestre estudiante 4: ', e_4['ssc'])

# Retornar un diccionario que tenga la información de los estudiantes que están en riesgo, es decir, cuyo promedio sea menor a tres cuatro.

def quienes_en_riesgo(est1, est2, est3, est4):
    en_riesgo = {}

    if est1['promedio'] < 3.4:
        en_riesgo[est1['nombre']] = est1['promedio']
    if est2['promedio'] < 3.4:
        en_riesgo[est2['nombre']] = est2['promedio']
    if est3['promedio'] < 3.4:
        en_riesgo[est3['codigo']] = est3['promedio']
    if est4['promedio'] < 3.4:
        en_riesgo[est4['codigo']] = est4['promedio']
    
    return en_riesgo

riesgo = quienes_en_riesgo(e_1, e_2, e_3, e_4)

print(riesgo)