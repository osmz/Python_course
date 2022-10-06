import calculadora_indices as calc

def iniciar_aplicacion():
    peso = int(input('Ingrese el peso de la persona (en Kilogramos): '))
    altura = int(input('Ingrese la altura de la persona (en centimetros): '))
    edad = int(input('Ingrese la edad de la persona (en años): '))
    valor_genero = float(input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
    valor_actividad = float(input('''Ingrese el valor actividad dependiendo de la actividad fisica que se lleva a cabo: 
    • 1.2: poco o ningún ejercicio
    • 1.375: ejercicio ligero (1 a 3 días a la semana)
    • 1.55: ejercicio moderado (3 a 5 días a la semana)
    • 1.72: deportista (6 -7 días a la semana)
    • 1.9: atleta (entrenamientos mañana y tarde): '''))

    TMB_actividad_fisica = round(calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad), 2)
    print('El número de calorías que un usted quema al día estando en reposo es de : ', TMB_actividad_fisica, 'cal')

iniciar_aplicacion()