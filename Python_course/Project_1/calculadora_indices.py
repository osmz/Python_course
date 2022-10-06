# Algoritmo para crear una aplicación que permite hacer cálculos de distintos índices corporales como el índice de masa corporal y la tasa metabólica basal.

# En el desarrollo de este proyecto mostrarás tu capacidad para: 
#   Crear funciones.
#   Llamar funciones con parámetros.
#   Llamar funciones desde otras funciones (composición de funciones).
#   Crear y usar un módulo.
#   Probar las funciones de un módulo. 
#   Construir interfaces de usuario basadas en consola.

def calcular_IMC(peso, altura):
    IMC = peso/altura**2
    return IMC

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    IMC = peso/altura**2
    GC = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero
    return GC

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    TMB_actividad_fisica = TMB * valor_actividad
    return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return TMB
