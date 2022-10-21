# Queremos poder construir una frase, a partir de dos cadenas, intercalando una palabra de una cadena, con una palabra de la otra comenzando con la primera palabra de la primera cadena. Por ejemplo, si tenemos las cadenas, la casa está cerca río, y, linda no muy del grande, el resultado de la intercalación sería la frase, la linda casa no está muy cerca del río grande.

def intercalar_palabras(cad1, cad2):
    resultado = ''

    palabras_1 = cad1.split()
    palabras_2 = cad2.split()

    for i in range(0, len(palabras_1)):
        resultado += (palabras_1[i] +' '+palabras_2[i]+' ')

    return resultado

c_1 = 'La casa está cerca río'
c_2 = 'linda no muy del grande'

print(intercalar_palabras(c_1, c_2))