import calculadora_indices as calc

def iniciar_aplicacion():
    peso = int(input('Ingrese el peso de la persona (en Kilogramos): '))
    altura = float(input('Ingrese la altura de la persona (en metros): '))
    IMC = round(calc.calcular_IMC(peso, altura), 2)
    print('Su indice de masa corporal (IMC) es: ', IMC)

iniciar_aplicacion()