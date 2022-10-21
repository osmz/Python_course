#  programa completo que nos permita crear listas ordenadas de "strings"

def insertar_ordenado(lista_ordenada, cadena):
    i = 0

    while i < len(lista_ordenada) and cadena > lista_ordenada[i]:        
        i += 1

    lista_ordenada.insert(i, cadena)

    return lista_ordenada

def ordenar_lista(lista_desordenada):
    ordenada = []

    for cadena in lista_desordenada:
        ordenada = insertar_ordenado(ordenada, cadena)

    return ordenada

lista = []
palabra = input("Ingrese una cadena, o 'terminar' para cerrar: ")

while palabra != 'terminar':
    insertar_ordenado(lista, palabra)
    palabra = input("Ingrese una cadena, o 'terminar' para cerrar: ")

print(lista)

lista = ['tanque', 'avión', 'moto', 'automóvil', 'barco', 'diligencia']

orden =  ordenar_lista(lista)

print(orden)

