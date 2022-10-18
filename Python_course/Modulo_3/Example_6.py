# Crear una función que nos permita saber si el número es o no primo. Recordemos, que un número primo es aquel número mayor a uno que solo es divisible en uno y en sí mismo.

def es_numero_primo(numero):
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    
    return primo

print(es_numero_primo(16))