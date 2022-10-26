# Campeonato de futbol

def total_goles(tablero_goles):
    total = 0

    for i in range(len(tablero_goles)):
        for j in range(len(tablero_goles[0])):
            casilla = tablero_goles[i][j]
            if casilla >= 0:
                total += casilla
    
    return total

def partidos_jugados(tablero_goles):
    partidos = 0

    for i in range(len(tablero_goles)):
        for j in range(i+1, len(tablero_goles[0])):
            if tablero_goles[i][j] >= 0:
                partidos += 1
        
    return partidos

def equipo_mas_goleador(tablero_goles, equipos):
    max_goles = 0
    indice_goleador = 0

    for i in range(len(tablero_goles)):
        goles_actual = 0
        for j in range(len(tablero_goles[0])):
            if tablero_goles[i][j] > 0:
                goles_actual += tablero_goles[i][j]

        if goles_actual > max_goles:
            max_goles = goles_actual
            indice_goleador = i
        
    nom_equipo = ''

    for eq in range(len(equipos)):
        if eq == indice_goleador:
            nom_equipo = equipos[eq]   

    #for eq in equipos:
    #    if equipos[eq] == indice_goleador:
    #        nom_equipo = equipos[eq]      
    
    return nom_equipo

tablero_goles = [[-1,2,3,0,-2,1,-2,0],
                [1,-1,1,3,2,-2,0,0],
                [5,1,-1,2,3,4,2,1],
                [1,4,2,-1,1,5,2,1],
                [-2,4,2,3,-1,2,1,3],
                [2,-2,2,3,1,-1,4,1],
                [-2,1,4,1,2,3,-1,-2],
                [1,4,2,1,0,0,-2,-1]]

equipos= ['AJA','JUV','MANU','BAR','MANC','TOT','LIV','POR']

print(total_goles(tablero_goles))
print(partidos_jugados(tablero_goles))
print(equipo_mas_goleador(tablero_goles, equipos))