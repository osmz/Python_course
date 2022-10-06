import calculadora_indices as calc

def iniciar_aplicacion():
    peso = int(input('Ingrese el peso de la persona (en Kilogramos): '))
    altura = float(input('Ingrese la altura de la persona (en metros): '))
    edad = int(input('Ingrese la edad de la persona (en años): '))
    valor_genero = float(input('Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: '))
    GC = round(calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero), 2)
    print('Su porcentaje de grasa corporal es: ', GC, '%')

iniciar_aplicacion()