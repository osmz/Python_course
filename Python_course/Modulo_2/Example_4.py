# Función que recibe dos números enteros n y d y determina si n es divisible por 2d, si n es divisible por d, o si n no es divisible ni por d ni por 2d.

# Recordar que ningún número es divisible por 0.

def es_divisible(n, d):
    if d > 0:
        if (n % (2*d)) == 0:
            resultado = 2
        elif (n % d) == 0 and (n % (2*d)) != 0:
            resultado = 1
        else:
            resultado = 0
    else:
        resultado = 0

    return resultado

print(es_divisible(2, 2))

