# Una agencia de viajes necesita informar a sus clientes la hora de llegada de sus vuelos. Se conoce la hora de partida del vuelo (en horas, minutos y segundos) y la duración del vuelo (en horas, minutos y segundos).

# Cree una función que retorne la hora de llegada del vuelo en una cadena con el formato “HH:mm:ss” donde HH es la hora, mm los minutos y ss los segundos de la hora de llegada del vuelo. 

# La hora está dada en formato de 24 horas. Si alguno de los 3 números de la respuesta es menor a 10, sólo se necesita un dígito ('7' en lugar de '07').

def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):
    hora_llegada = (hora_salida + duracion_horas)*3600
    minuto_llegada = (minuto_salida + duracion_minutos)*60
    segundo_llegada = (segundo_salida + duracion_segundos)

    if segundo_llegada > 59:
        minuto_llegada = minuto_llegada + 60
        segundo_llegada = segundo_llegada - 60

    if minuto_llegada > 3599:
        hora_llegada = hora_llegada + 3600
        minuto_llegada = minuto_llegada - 3600

    if hora_llegada == 0 or hora_llegada > 86399:
        hora_llegada = hora_llegada - 86400

    hora_final = int(hora_llegada/3600)
    minuto_final = int(minuto_llegada/60)

    return (str(hora_final)+":"+str(minuto_final)+":"+str(segundo_llegada))

print ("La hora de llegada de su vuelo es: ", calcular_horario_llegada(5, 30, 30, 6, 38, 45))