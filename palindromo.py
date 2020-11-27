def palindormo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertido = palabra[::-1]
    if palabra == palabra_invertido:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindormo(palabra)
    if es_palindromo == True:
        print("Es palindormo")
    else:
        print("No es palindrono")


if __name__ =="__main__":
    run()