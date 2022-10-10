# En el taller de regalos de Santa Claus, el CTE (Chief Technology Elf) ha decidido implementar un nuevo sistema de clasificación de regalos, para facilitar su organización. Cada paquete tiene ahora un identificador numérico único. El identificador es un número entero entre 100 y 999 y sirve para clasificar los regalos de la siguiente manera.

# Si el número es palíndromo e impar, el regalo corresponde a una niña.

# Si el número es palíndromo y par, el regalo corresponde a un niño.

# Si el número es par pero no es palíndromo, el regalo corresponde a un hombre.

# Si el número es impar pero no es palíndromo, el regalo corresponde a una mujer.

# Escriba una función que ayude al CTE a calcular, dado un identificador único de regalo, a qué tipo de persona corresponde dicho regalo.

import math 
   
def rev(id):
    return int(id != 0) and ((id % 10) * (10**int(math.log(id, 10))) + rev(id // 10)) 

def clasificar_regalo(id):
    numero_invertido = rev(id)
    palindromo = False
    if id == numero_invertido:
        palindromo = True
    
    if palindromo == True and id % 2 == 1:
        regalo = 'girl'
    elif palindromo == True and id % 2 == 0:
        regalo = 'boy'
    elif id % 2 == 0 and palindromo == False:
        regalo = 'man'
    elif id % 2 == 1 and palindromo == False:
        regalo = 'woman'
    
    return regalo

print(clasificar_regalo(242))
