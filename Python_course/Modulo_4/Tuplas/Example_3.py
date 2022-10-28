# Construya una función que reciba como parámetros un texto (cadena de caracteres) y una lista de caracteres permitidos (lista de cadenas de caracteres), y que retorne un diccionario con información sobre las palabras contenidas en el texto. 

# La función debe construir un diccionario en el que las llaves son todas las palabras que aparecen en el texto, ignorando si en el texto aparecen en mayúsculas o minúsculas. Sin embargo, las llaves del diccionario deben ser sólo cadenas en minúscula.

# Cada una de las llaves, debe tener asociada una tupla con tres valores de tipo entero: el primero indica la cantidad de veces que aparece la palabra en el texto, el segundo indica la primera posición en la que aparece la palabra, y el tercero indica la última posición en la que aparece. Si la palabra aparece una sola vez en el texto, el segundo y el tercer valor serán iguales.

# La lista de caracteres permitidos indica qué caracteres pueden hacer parte de las palabras, cualquier carácter que no haga parte de esta lista debe tratarse como si fuera un espacio o un signo de puntuación.

# Nota: las posiciones hacen referencia a las posiciones en el texto original que la función recibe como parámetro, contadas desde 0.

# Veamos un ejemplo en el que los caracteres permitidos son todos los caracteres del español, incluyendo las vocales acentuadas. Suponga que el texto que se va a analizar es el siguiente: "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."

# En el diccionario resultante deben aparecer las siguientes palabras, de las cuales sólo dos se repiten: 'a', 'al', 'aquella', 'aureliano','años', 'buendía', 'conocer', 'coronel', 'de', 'después', 'el', 'en','frente', 'fusilamiento', 'había', 'hielo', 'llevó', 'lo', 'muchos', 'padre', 'pelotón', 'que', 'recordar', 'remota', 'su', 'tarde'.

# La palabra 'el' aparece dos veces en el texto, la primera a partir de la posición 56 y la segunda a partir de la posición 159. Tenga cuidado, la aparición de la cadena 'el' dentro de la palabra 'hielo' no se tiene en cuenta porque no es una palabra completa.

# La otra palabra que se repite en este texto es la palabra 'de', que aparece a partir de las posiciones 39 y 91. Tenga cuidado de no contar la aparición de la sílaba 'de' en la palabra 'después'.

def analizar_texto(texto, caracteres_permitidos):
    texto_original = texto
    texto_minusculas = texto_original.lower() 
    texto_minusculas = texto_minusculas.replace(","," ").replace("."," ")

    lista_caracteres = ''.join(caracteres_permitidos)

    for i in range(len(texto_minusculas)):
        palabra = texto_minusculas[i]
        caracter = lista_caracteres.find(palabra)
        if caracter == -1 and palabra != ' ':
            texto_minusculas = texto_minusculas.replace(palabra, ' ')

    lista_Palabras = texto_minusculas.split()

    frecuencia_Palabras = []
    posicion_inicial = []
    posicion_final = []
    for palabra in lista_Palabras:
        frecuencia = lista_Palabras.count(palabra)
        frecuencia_Palabras.append(lista_Palabras.count(palabra))

        lst_palabra = []
        for j in range(len(palabra)):
                lst_palabra.append(palabra[j])
        buscar_palabra = ''.join(lst_palabra)

        if frecuencia >= 2 and buscar_palabra == lista_Palabras[0]:
            lst_palabra_aux = []
            for j in range(len(palabra)):
                lst_palabra_aux.append(palabra[j])
                
            lst_palabra_aux.append(' ')
            print('lst_palabra_aux')
            print(lst_palabra_aux)
            buscar_palabra_aux = ''.join(lst_palabra_aux)
            
            posicion_inicial.append(texto_minusculas.find(buscar_palabra_aux))
            posicion_final.append(texto_minusculas.rfind(buscar_palabra_aux))
        elif frecuencia == 1 and buscar_palabra == lista_Palabras[-1]:
            lst_palabra_aux = []
            lst_palabra_aux.append(' ')
            for j in range(len(palabra)):
                lst_palabra_aux.append(palabra[j])
            
            print('lst_palabra_aux')
            print(lst_palabra_aux)
            buscar_palabra_aux = ''.join(lst_palabra_aux)
            
            posicion_inicial.append(texto_minusculas.find(buscar_palabra_aux) + 1)
            posicion_final.append(texto_minusculas.rfind(buscar_palabra_aux) + 1)
        else:
            lst_palabra_aux = []
            lst_palabra_aux.append(' ')
            for j in range(len(palabra)):
                lst_palabra_aux.append(palabra[j])
            
            lst_palabra_aux.append(' ')
            print('lst_palabra_aux')
            print(lst_palabra_aux)
            buscar_palabra_aux = ''.join(lst_palabra_aux)
            
            posicion_inicial.append(texto_minusculas.find(buscar_palabra_aux) + 1)
            posicion_final.append(texto_minusculas.rfind(buscar_palabra_aux) + 1)

    tupla = list(zip(frecuencia_Palabras, posicion_inicial, posicion_final))

    dict = {}
    for i in  range(len(lista_Palabras)):
        dict[lista_Palabras[i]] = tupla[i]

    return dict

#texto = 'Muchos años de el de el hielo'
#texto = 'Muchos años después frente al pelotón de fusilamiento el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo'
#texto = 'Seis suecos sosos secan sesos sin sal, Secan seis sesos los suecos, Salan seis sesos con sal, secan y salan los sesos, que sacan del secadal'
texto = 'Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo'
#caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']
#caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']
caracteres_permitidos = ['*']
print(analizar_texto(texto, caracteres_permitidos))
