# Crear un programa que nos permita contabilizar los votos de las elecciones presidenciales de los Estados Unidos. Para representar los votos, se ha decidido utilizar una lista de tuplas, donde cada voto es representado por una tupla, que incluye un identificador único de voto, el nombre del candidato por quién se ha votado, el estado del cual provienen el voto y el condado dentro del estado al que pertenece el voto. 

# Primero la cantidad de votos recibidos por cada candidato en un determinado estado del país. Esta información se debe retornar como una tupla. Segundo se quiere poder conocer la cantidad de votos recibidos por cada candidato, en cada uno de los 50 estados del país. La información debe retornar se en un diccionario, cuyas llaves son los nombres de los estados y los valores son tuplas con la cantidad de votos recibidos por cada candidato en el estado. 

def contar_votos_estado(votos, estado_interes):
    cant_votos_trump = 0
    cant_votos_biden = 0

    for voto_actual in votos:
        id_voto, candidato, estado, condado = voto_actual

        if estado == estado_interes:
            if candidato == 'Donald Trump':
                cant_votos_trump += 1
            else:
                cant_votos_biden += 1
    
    return (cant_votos_trump, cant_votos_biden)

def contar_total_votos_por_estado(votos, estados):
    totales_estado = {}

    for i in range(len(estados)):
        estado_actual = estados[i]
        votos_estado_actual = contar_votos_estado(votos, estado_actual)
        totales_estado[estado_actual] = votos_estado_actual
    
    return totales_estado

import random

estados = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Carolina', 'Carolina', 'Colorado', 'Connecticut', 'Dakota', 'Dakota', 'Delaware ', 'Florida', 'Georgia','Hawái', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Luisiana', 'Maine', 'Maryland', 'Massachusetts', 'Míchigan', 'Minnesota', 'Misisipi', 'Misuri', 'Montana', 'Nebraska', 'Nevada', 'Nueva Jersey', 'Nueva York', 'Nuevo Hampshire', 'Nuevo México', 'Ohio', 'Oklahoma', 'Oregón', 'Pensilvania', 'Rhode Island', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Virginia Occidental', 'Washington', 'Wisconsin', 'Wyoming')

votos = []

for est in estados:
    cant_votos = random.randint(4000, 8000)
    for i in range(cant_votos):
        elegido = random.randint(0,1)
        candidato = 'Donald Trump'
        if elegido == 1:
            candidato = 'Joe Biden'
        id_voto = est + str(i)
        voto = (id_voto, candidato, est, 'Some Country')
        votos.append(voto)

cuenta = contar_total_votos_por_estado(votos, estados)

for estado in cuenta:
    print(estado, '\nTotal ->', 'Trump: ', str(cuenta[estado][0]), 'Biden: ' + str(cuenta[estado][1]) + '\n')


