# ejercicio con algunos condicionales más complejos para seguir reforzando el tema. Nos piden crear un programa que permita calcular el valor del pasaje aéreo desde la ciudad de Bogotá hasta Tokio.

# El valor dependerá de una tarifa básica, la compañia aérea elegida para el viaje, la temporada, la edad del pasajero y si es o no estudiante. Para calcular el precio, nos dicen que tenemos que tener en cuenta que la compañía ALAS incremente el valor de sus pasajes en un 30% en alta temporada, mientras que la compañía VOLAR lo incrementa solo en 20%. 

# Ambas compañías descuentan el 50% si el pasajero es menor de edad. Además, la compañía VOLAR tiene un recargo de 100.000 pesos para los pasajeros mayores de 60 años para cubrir el seguro de vida.

# Los estudiantes que viajan por ALAS y que no son menores de edad tienen un descuento de 10% en temporada baja. 

# Y la tarifa básica Bogotá-Tokio reglamentaria es de 5.000.000 de pesos. 

def calcular_precio_pasaje(temporada_alta, compania, edad, estudiante):
    precio = 5000000
    variaciones = 0
    seguro = False

    if compania == 'ALAS':
        if temporada_alta:
            variaciones += 0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -= 0.1
    elif compania == 'VOLAR':
        if temporada_alta:
            variaciones += 0.2
        if edad > 60:
            seguro = True
    
    if edad < 18:
        variaciones -= 0.5
    
    precio *= (1 + variaciones)

    if seguro:
        precio += 100000
    
    return round(precio)

temp = bool(int(input('¿Es temporada alta? Ingrese 1 para SI o 0 para NO: ')))
compania = input('Ingrese la compañia por la que viajrá: ')
edad = int(input('Ingrese la edad de la persona: '))
est = bool(int(input('¿Es estudiante? Ingrese 1 para SI o 0 para NO: ')))

tarifa = calcular_precio_pasaje(temp, compania, edad, est)

print('La tarifa del pasaje es de $' + str(tarifa)+ ' COP')