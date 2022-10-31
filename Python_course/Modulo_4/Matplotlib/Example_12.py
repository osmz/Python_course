# analizar las notas obtenidas por los estudiantes de una materia en una universidad. De cada estudiante tenemos su nota y el código que lo identifica en la institución. Utilizaremos Matplotlib para generar unas gráficas que nos permitan estudiar las notas. Crearemos tres tipos de gráficas: una "Gráfica de línea" o "line plot", un "Histograma" y una "Gráfica de Dispersión" o "Scatter plot".

import random
import matplotlib.pyplot as plt

notas = []
ids_estudiantes = []

for i in range(30):
    nota_generada = random.normalvariate(3.25, 0.98)
    nota_generada = round(nota_generada, 2)
    agregado = False
    while not agregado:
        id_generado = random.randint(20202001, 20202999)
        id_generado = str(id_generado)
        if id_generado not in ids_estudiantes:
            notas.append(nota_generada)
            ids_estudiantes.append(id_generado)
            agregado = True

plt.figure()
plt.plot(ids_estudiantes, notas)
plt.title('Notas de curso')
plt.xlabel('ID estudiante')
plt.xticks(rotation = 90)
plt.ylabel('Notas')

plt.figure()
plt.hist(notas, bins = 4, color = ['green'], edgecolor = 'black', linewidth = 1)
plt.title('Cantidad de estudiantes por rango de nota')
plt.ylabel('Cantidad de estudiante')
plt.xlabel('Rango nota')

plt.figure()
plt.scatter(ids_estudiantes, notas)
plt.title('Notas de curso')
plt.xlabel('ID estudiante')
plt.xticks(rotation = 90)
plt.ylabel('Notas')
plt.show()
