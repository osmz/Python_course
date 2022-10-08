# Ejemplo de front-end and back-end

import ft_example_6 as E6;

def ejecutar_converir_a_dolares(trm):
    pesos = float(input('Ingrese la cantidad de pesos: '))
    dolares = E6.convertir_a_dolares(pesos, trm)
    print(pesos, 'pesos son', round(dolares, 2), 'dolares')

def ejecutar_converir_a_pesos(trm):
    dolares = float(input('Ingrese la cantidad de dolares: '))    
    pesos = E6.convertir_a_pesos(dolares, trm)
    print(dolares, 'dolares son', round(pesos, 2), 'pesos')

def mostrar_menu():
    print('Seleccione una opcion:')
    print('1. Converir de dólares a pesos')
    print('2. Converir de pesos a dólares')
    opcion = input('Opcion seleccionada: ')
    return opcion

def iniciar_aplicacion():
    opcion = mostrar_menu()    
    trm = float(input('Ingrese la TRM: '))
    if opcion == '1':
        ejecutar_converir_a_pesos(trm)
    elif opcion == '2':
        ejecutar_converir_a_dolares(trm)
    else:
        print('La opciõn nseleccionada no es válida')

iniciar_aplicacion()
    
