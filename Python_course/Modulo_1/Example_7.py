# Crea una función que calcule la edad de una persona a partir de su fecha de nacimiento y la fecha actual.

# Ambas fechas se proporcionan en años, meses y días, y la edad debe retornarse de la misma manera, en una cadena con la forma “aa,MM,dd”. Suponga que todos los meses son de 30 días.

# Por ejemplo, si Julieta Pérez nació el 20 de noviembre de 1986, y la fecha actual fuese el 16 de octubre de 1987, la función retornaría que la edad de Julieta es “0,10,26”, es decir, 0 años, 10 meses y 26 días.

def calcular_edad(dia_nacio, mes_nacio, anio_nacio, dia_actual, mes_actual, anio_actual):
    anio = anio_actual - anio_nacio
    #print('anio')
    #print(anio)
    mes = 12 - mes_nacio
    mes = mes + mes_actual
    #print('mes')
    #print(mes)
    dia = 30 - dia_nacio
    dia = dia + dia_actual
    #print('dia')
    #print(dia)

    if mes_nacio > mes_actual or mes_nacio == mes_actual:
        anio -= 1
        #print('anio1')
        #print(anio)
    
    if dia_nacio > dia_actual:
        mes -= 1
        #print('mes2')
        #print(mes)
    elif dia == 30:
        mes = 0
        #dia = dia - 30
        #print('mes3')
        #print(mes)
    
    if mes > 12:
        mes -= 12
        #print('mes4')
        #print(mes)
    
    if mes_nacio == mes_actual and anio_nacio == anio_actual:
        #print('entro')
        dia = dia_actual - dia_nacio
        mes = 0
        anio = 0
    
    if anio_nacio == anio_actual and dia < 30:
        #print('entro1')
        mes = 0
        anio = 0
    elif anio_nacio == anio_actual and dia > 30:
        #print('entro2')
        dia = dia - 30
        mes = mes_actual - mes_nacio
        anio = 0
    elif anio_nacio == anio_actual and dia == 30:
        #print('entro3')
        dia = dia - 30
        mes = mes_actual - mes_nacio
        anio = 0
     
    if dia == 30 and dia_nacio == dia_actual and mes_nacio != mes_actual:
        dia = dia - 30
        mes = 12 - mes_nacio
        mes = mes + mes_actual

    return (str(anio)+","+str(mes)+","+str(dia))

print ("Su edad es: ", calcular_edad(20, 11, 1986, 16, 10, 1987))
print ("Su edad es: ", calcular_edad(15 , 2, 1993, 15, 2, 2023))
print ("Su edad es: ", calcular_edad(15 , 2, 1993, 6, 10, 2022))
print ("Su edad es: ", calcular_edad(25, 11, 1991, 6, 10, 2022))
print ("Su edad es: ", calcular_edad(5, 8, 2019, 15, 8, 2019))
print ("Su edad es: ", calcular_edad(25, 10, 1993, 4, 8, 2019))
print ("Su edad es: ", calcular_edad(28, 3, 2004, 10, 4, 2004))
print ("Su edad es: ", calcular_edad(5, 8, 2019, 5, 9, 2019))
print ("Su edad es: ", calcular_edad(1, 1, 1970, 14, 2, 1970))
print ("Su edad es: ", calcular_edad(28, 12, 2004, 28, 3, 2005))