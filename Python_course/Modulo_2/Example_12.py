# El juego de las Picas y Fijas es un juego matemático muy sencillo, consiste en adivinar un número de 4 cifras y de todos los dígitos diferentes. Para esto, el jugador que intenta adivinar deberá decir el número que cree está escondiendo el otro, y este deberá responder el número de picas y fijas que tiene ahora el jugador.

# Una pica es un dígito que se encuentra en el número a adivinar, pero no está en el lugar correcto; y una fija es un dígito correctamente colocado.

# Por ejemplo, si el número secreto es 1234 y el otro jugador dice 1325, tendrá dos picas y una fija.

# Debes crear una función que devuelva un diccionario con las llaves "PICAS" y "FIJAS" que represente el resultado de la jugada si un jugador trata de adivinar el numero_secreto con el número intento

def picas_y_fijas(numero_secreto, intento):
    diccionario = {"PICAS": 0, "FIJAS": 0}
    num_ref = numero_secreto
    while intento > 0:
        i = num_ref % 10 # ultima cifra
        #print('i')
        #print(i)
        j = intento % 10 # ultima cifra
        #print('j')
        #print(j)
        if i == j:
            diccionario["FIJAS"] += 1
            #print('diccionario')
            #print(diccionario)
        elif str(j) in str(numero_secreto):
            #print('j')
            #print(j)
            diccionario["PICAS"] += 1
            #print('diccionario')
            #print(diccionario)
        num_ref = num_ref // 10 # Se elimina la ultima cifra
        #print('num_ref')
        #print(num_ref)
        intento = intento // 10 # idem
        #print('intento')
        #print(intento)

    return diccionario

print(picas_y_fijas(1234, 1325))