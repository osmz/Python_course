import calculadora_indices as calc

def iniciar_aplicacion():
    peso = int(input('Ingrese el peso de la persona (en Kilogramos): '))
    altura = int(input('Ingrese la altura de la persona (en centimetros): '))
    edad = int(input('Ingrese la edad de la persona (en años): '))
    valor_genero = float(input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
    TMB = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print('Para adelgazar es recomendado que consumas entre: ', round(TMB*0.80, 2), ' y ' , round(TMB*0.85, 2), 'calorías al día.')

iniciar_aplicacion()