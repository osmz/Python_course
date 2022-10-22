# Nicolás es un novio muy amoroso, pero tiene fama de ser tacaño. Para el cumpleaños de su novia ha pedido un catálogo de artículos para escoger el regalo más barato disponible. El catálogo es un diccionario que tiene varias llaves que corresponden al nombre de los productos. El valor asociado a cada llave es el precio del producto.

# Cree una función que retorne el nombre del artículo más barato en el catálogo.

# Si Nicolás encuentra dos artículos igual de baratos, comprará el que tenga el nombre alfabéticamente menor (el que aparecería antes en el diccionario ignorando las mayúsculas y minúsculas).

# Si el artículo más barato vale más de 10.000 pesos, Nicolás no comprará nada e invitará a su novia a ver una película en su casa.  

def producto_mas_barato(catalogo):  
    barato = []  
    if len(catalogo) > 0:    
        list_catalogo_keys = list(catalogo.keys())
        list_catalogo_values = list(catalogo.values())
        min_catalogo = min(list_catalogo_values)

        for i in range(len(list_catalogo_values)):
            if min_catalogo == list_catalogo_values[i]:
                dic_barato = list_catalogo_keys[i]
                barato.append(dic_barato)
            
        if len(barato) == 0:
            mas_barato = barato
        else:
            mas_barato = min(list(barato))

        if min_catalogo > 10000:
            mas_barato = None
    else:
        mas_barato = 'No hay productos para escoger'
    
    return mas_barato


print(producto_mas_barato(catalogo = {'pantuflas': 20000, 'chicle': 2000, 'coca cola': 2500, 'lenceria': 7000}))
print(producto_mas_barato(catalogo = {'pantuflas': 2000, 'chicle': 2000, 'arbol': 2000, 'lenceria': 7000}))
print(producto_mas_barato(catalogo = {'pantuflas': 20000, 'chicle': 3000, 'coca cola': 2500, 'lenceria': 7000}))
print(producto_mas_barato(catalogo = {}))