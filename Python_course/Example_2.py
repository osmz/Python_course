# Problema que solicita al usuario una cantidad de pesos, una tasa de interés y un número de años. Muestra por pantalla en cuánto se habrá convertido el capital inicial transcurrido esos años si cada año se aplica la tasa de interés introducida.
# Recuerde que un capital de C pesos a un interés del x por cien durante n años se convierte en C*(1+ x/100)^n pesos. Pruebe su programa sabiendo que una cantidad de 10.000 oesis al 4.5% de interés anual se convierte en 24.1117,14 pesos al cabo de 20 años.

capital = float(input('Ingrese el capital inicial: '))
tasa = float(input('Ingrese la tasa anual: '))
tiempo = int(input('Ingrese el numero de años: '))

valorFuturo = capital * (1 + (tasa/100)) ** tiempo

print('El valor futuro del monto inicial es de $' + str(valorFuturo) + ', transcurrido ' + str(tiempo) + ' años y a una tasa del ' + str(tasa) + '% anual')