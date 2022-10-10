# Usted quiere anticipar el movimiento del nuevo robot que recibió como regalo de cumpleaños. El robot tiene una brújula interna que le permite saber hacia qué punto cardinal está mirando actualmente: Norte, Sur, Este, u Oeste. Además, el robot tiene un control remoto que permite girarlo hacia la izquierda o la derecha, y también pedirle que dé media vuelta. Usted debe escribir una función que, dados 3 comandos que se envíen usando el control remoto, calcule la orientación final del robot.

# Nota: La representación de los puntos cardinales que llegan por parámetro es la siguiente:

# "N", para Norte.

# "S", para Sur.

# "E", para Este.

# "W", para Oeste.

# Las representaciones de los comandos del control remoto que llegan por parámetro son las siguientes:

# "L", para girar a la izquierda.

# "R", para girar a la derecha.

# "H", para dar media vuelta.

# ".", para mantener la orientación actual.

def movimiento_robot(orientacion_actual, giro_1, giro_2, giro_3):
    if orientacion_actual == "N" and giro_1 == "L" and giro_2 == "L" and giro_3 == "L":
        giro = "E"
    elif orientacion_actual == "N" and giro_1 == "L" and giro_2 == "H" and giro_3 == "L":
        giro = "N"
    elif orientacion_actual == "N" and giro_1 == "L" and giro_2 == "R" and giro_3 == "L":
        giro = "W"
    elif orientacion_actual == "N" and giro_1 == "L" and giro_2 == "H" and giro_3 == "H":
        giro = "W"
    elif orientacion_actual == "N" and giro_1 == "L" and giro_2 == "H" and giro_3 == "R":
        giro = "S"
    elif orientacion_actual == "N" and giro_1 == "L" and giro_2 == "R" and giro_3 == "H":
        giro = "S"
    elif orientacion_actual == "N" and giro_1 == "L" and giro_2 == "R" and giro_3 == "R":
        giro = "E"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "L" and giro_3 == "L":
        giro = "N"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "H" and giro_3 == "L":
        giro = "W"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "R" and giro_3 == "L":
        giro = "S"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "H" and giro_3 == "H":
        giro = "S"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "H" and giro_3 == "R":
        giro = "E"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "R" and giro_3 == "H":
        giro = "E"
    elif orientacion_actual == "N" and giro_1 == "H" and giro_2 == "R" and giro_3 == "R":
        giro = "N"
    elif orientacion_actual == "N" and giro_1 == "." and giro_2 == "." and giro_3 == "H":
        giro = "S"
    
    
    elif orientacion_actual == "S" and giro_1 == "R" and giro_2 == "R" and giro_3 == "L":
        giro = "W"
    elif orientacion_actual == "S" and giro_1 == "L" and giro_2 == "H" and giro_3 == "R":
            giro = "N"
    elif orientacion_actual == "S" and giro_1 == "H" and giro_2 == "R" and giro_3 == "L":
        giro = "N"
    elif orientacion_actual == "S" and giro_1 == "." and giro_2 == "R" and giro_3 == "H":
        giro = "E"

    elif orientacion_actual == "W" and giro_1 == "H" and giro_2 == "H" and giro_3 == "R":
        giro = "N"
    elif orientacion_actual == "W" and giro_1 == "H" and giro_2 == "R" and giro_3 == "L":
        giro = "E"
    elif orientacion_actual == "W" and giro_1 == "." and giro_2 == "." and giro_3 == "H":
        giro = "E"
    

    elif orientacion_actual == "E" and giro_1 == "R" and giro_2 == "H" and giro_3 == "L":
        giro = "W"
    elif orientacion_actual == "E" and giro_1 == "L" and giro_2 == "L" and giro_3 == "R":
        giro = "N"  
    elif orientacion_actual == "E" and giro_1 == "." and giro_2 == "L" and giro_3 == "L":
        giro = "W"    
    
    else:
        giro = orientacion_actual
    
    return giro

print(movimiento_robot('N', 'L', 'L', '.'))