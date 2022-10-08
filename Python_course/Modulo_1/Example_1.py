# Problema que rota los valores de 3 variables enteras x1, x2, x3 hacia la derecha de forma que al final x2 tendra el valor inicial de x1, x3 el de x2 y x1 el de x3.

x1 = int(input('Ingrese el valor de x1: '))
x2 = int(input('Ingrese el valor de x2: '))
x3 = int(input('Ingrese el valor de x3: '))

temporal = x1
x1 = x3
x3 = x2
x2 = temporal

print(str(x1) + ', ' + str(x2) + ', ' + str(x3))