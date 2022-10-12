# Escriba una función que determine si en dos números enteros aparecen los mismos dígitos. No tenga en cuenta ni la frecuencia ni el orden de aparición de los dígitos en los números.

# Los números no tienen necesariamente la misma cantidad de dígitos. Por ejemplo, si los números son 998 y 89 la función debería retornar True.

def mismos_digitos(a, b):
    if b > a:
        aux_b = b
        b = a
        a = aux_b

    a = str(a)
    b = str(b)
    mismos = True
    #for i in range(len(str(b))):
    i = 0
    while i <= len(str(b)):
        c = a.find(str(b[i - 1]))
        if c < 0:
            mismos = False
        i += 1

    return mismos
        
 
print(mismos_digitos(1234, 12345))