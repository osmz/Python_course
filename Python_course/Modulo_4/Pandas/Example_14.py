#  Representar las notas de los estudiantes de un curso mediante una serie de Pandas. Teniendo esto en cuenta, implementaremos una función que permita aumentar las notas. Si la media de estas es mayor a 2.5, el aumento deberá ser de una desviación estándar y es importante recordar que la máxima nota es cinco. Así que si con el aumento alguna nota supera este valor, debemos asignarle cinco. La función tendrá que retornar entonces la serie con las notas incrementadas en caso que se haya podido aplicar el aumento.

import pandas as pd
import random

def subir_notas(notas):
    if notas.mean() > 2.5:
        notas = notas + round(notas.std(), 2)
        print(round(notas.std(), 2))
    
    for i in range(notas.size):
        nota_actual = notas.iloc[i]
        if nota_actual > 5:
            notas.iloc[i] = 5.0
    
    return notas

notas = []
for i in range(15):
    nota_generada = random.normalvariate(3.25, 0.98)
    nota_generada = round(nota_generada, 2)
    valida = False
    while not valida:
        if nota_generada >= 1.5 and nota_generada <= 5.0:
            valida = True
        else:
            nota_generada = random.normalvariate(3.25, 0.98)
            nota_generada = round(nota_generada, 2)
        
    notas.append(nota_generada)

serie_notas = pd.Series(notas)
print(serie_notas)
print('-'*15)
print(subir_notas(serie_notas))
    