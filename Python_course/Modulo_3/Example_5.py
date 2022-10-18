def es_palindromo(cadena):
    palindromo = False
    sin_espacios = cadena.replace(' ','')
    en_minus = sin_espacios.lower()

    i = 0
    j = len(en_minus) - 1

    while i < j and en_minus[i] == en_minus[j]:
        i += 1
        j -= 1
    
    if i == j:
        palindromo = True
    
    return palindromo

print(es_palindromo('Isaac no ronca asi'))
print(es_palindromo('Sometamos o matemos'))
print(es_palindromo('Sometamos y matemos'))
