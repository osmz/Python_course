# Tus amigos, a quienes también les gusta mucho ver películas, te han propuesto ir al cine la próxima semana y quieren conocer los precios de las boletas.
# 
# Estas son las tarifas básicas de acuerdo con el tipo de sala:
# 
# Dinamix - 18800 pesos
# 
# 3D - 15500 pesos
# 
# 2D - 11300 pesos.
# 
# El cinema tiene, además, varias promociones que aplican para calcular el precio de las boletas que dependen del tipo de sala, del número de boletas que se compren simultáneamente, de la hora del día, del tipo de pago (tarjeta del cinema u otros medios de pago) y de si se tenía reserva.
# 
# Las promociones son las siguientes:
# 
# En las horas menos congestionadas (horas no pico) todas las salas tienen un descuento del 10% sobre la tarifa básica y si se compran 3 o más boletas, se aplican $500 pesos más de descuento por cada boleta
# 
# Si el medio de pago es la tarjeta del cinema, se hace un 5% descuento calculado sobre la tarifa básica
# 
# Cuando se hace una reserva, se tiene un recargo de $2000 pesos por boleta sin importar el tipo de sala
# 
# En las horas pico, la tarifa básica se incrementa un 25% para las salas 2D y 3D y un 50% para la sala Dinamix (este aumento no se tiene en cuenta para los recargos y descuentos).
# 
# Debes escribir una función que calcule cuánto te costarán las boletas para ti y tus amigos.

def calcular_costo_boletas(cantidad_boletas, tipo_sala, hora_pico, pago_tarjeta_cinema, reserva):
    dinamix = {'Valor': 18800}
    tres_D = {'Valor': 15500}
    dos_D = {'Valor': 11300}

    valor1_base = dinamix['Valor']
    valor2_base = tres_D['Valor']
    valor3_base = dos_D['Valor']

    var2 = False
    var3 = False

    if hora_pico == False:
        dinamix.update({'Valor': valor1_base - (round(valor1_base*0.1))})
        tres_D.update({'Valor': valor2_base - (round(valor2_base*0.1))})
        dos_D.update({'Valor': valor3_base - (round(valor3_base*0.1))})

        var1 = True
        if cantidad_boletas >= 3:
            valor1 = dinamix['Valor']
            valor2 = tres_D['Valor']
            valor3 = dos_D['Valor']

            dinamix.update({'Valor': valor1 - 500})
            tres_D.update({'Valor': valor2 - 500})
            dos_D.update({'Valor': valor3 - 500})

            var2 = True
    elif hora_pico == True:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 + (round(valor1*0.5))})
        tres_D.update({'Valor': valor2 + (round(valor2*0.25))})
        dos_D.update({'Valor': valor3 + (round(valor3*0.25))})

        var1 = True
    
    if pago_tarjeta_cinema == True and var1 == True and var2 == True:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 - (round(valor1_base*0.05))})
        tres_D.update({'Valor': valor2 - (round(valor2_base*0.05))})
        dos_D.update({'Valor': valor3 - (round(valor3_base*0.05))})

        var3 = True
    elif pago_tarjeta_cinema == True and var1 == True and var2 == False:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 - (round(valor1_base*0.05))})
        tres_D.update({'Valor': valor2 - (round(valor2_base*0.05))})
        dos_D.update({'Valor': valor3 - (round(valor3_base*0.05))})

        var3 = True
    elif pago_tarjeta_cinema == True and var1 == False and var2 == False:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 - (round(valor1_base*0.05))})
        tres_D.update({'Valor': valor2 - (round(valor2_base*0.05))})
        dos_D.update({'Valor': valor3 - (round(valor3_base*0.05))})

        var3 = True

    if reserva == True and var1 == True and var2 == True and var3 == True:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 + 2000})
        tres_D.update({'Valor': valor2 + 2000})
        dos_D.update({'Valor': valor3 + 2000})
    elif reserva == True and var1 == True and var2 == True and var3 == False:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 + 2000})
        tres_D.update({'Valor': valor2 + 2000})
        dos_D.update({'Valor': valor3 + 2000})
    elif reserva == True and var1 == True:
        valor1 = dinamix['Valor']
        valor2 = tres_D['Valor']
        valor3 = dos_D['Valor']

        dinamix.update({'Valor': valor1 + 2000})
        tres_D.update({'Valor': valor2 + 2000})
        dos_D.update({'Valor': valor3 + 2000})
    
    if tipo_sala == 'Dinamix':
        valor = dinamix['Valor']
    elif tipo_sala == '3D':
        valor = tres_D['Valor']
    else:
        valor = dos_D['Valor']

    return valor * cantidad_boletas

print(calcular_costo_boletas(1, '2D', False, True, True))