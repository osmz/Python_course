# Catalina necesita llevar un mejor control de sus gastos cuando hace mercado. Para esto, ha decidido construir una aplicación para registrar cada producto que agregue en su carrito de compras. Estos datos son guardados en un diccionario cuyas llaves corresponden a los nombres de los productos. El valor asociado a cada llave es el precio del producto correspondiente.

# Cree una función que retorne el valor total del carrito de compras. Esto es, la suma de los precios individuales de todos los productos que están en el carrito.  

def valor_carrito_compras(carrito_compras):

    if len(carrito_compras) > 0:
        list_carrito_compras_values = list(carrito_compras.values())
        total = sum(list_carrito_compras_values)
    else:
        total = 0
    
    return total