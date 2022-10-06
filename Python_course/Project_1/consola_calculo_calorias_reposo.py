import calculadora_indices as calc

def iniciar_aplicacion():
    peso = int(input('Ingrese el peso de la persona (en Kilogramos): '))
    altura = int(input('Ingrese la altura de la persona (en centimetros): '))
    edad = int(input('Ingrese la edad de la persona (en años): '))
    valor_genero = float(input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
    TMB = round(calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero), 2)
    print('El número de calorías que un usted quema al día estando en reposo es de : ', TMB, 'cal')

iniciar_aplicacion()