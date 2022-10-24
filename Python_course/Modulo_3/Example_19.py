# Catalina necesita llevar un mejor control de sus gastos cuando hace mercado. Para esto, ha decidido construir una aplicación para registrar cada producto que agregue en su carrito de compras. Estos datos son guardados en un diccionario cuyas llaves corresponden a los nombres de los productos. El valor asociado a cada llave es el precio del producto correspondiente.

# Cree una función que retorne el nombre del producto más costoso del carrito de compras. Si se encuentran dos productos igual de costosos (siendo los más costosos del carro), la función retorna el menor alfabéticamente. Por ejemplo, si los 'bananos' que compra Catalina costaran los mismo que las 'chocolatinas', la función retornaría 'bananos' 

def producto_mas_costoso(carrito_compras):
    costoso = []
    
    if len(carrito_compras) > 0:
        list_carrito_compras_values = list(carrito_compras.values())
        list_carrito_compras_keys = list(carrito_compras.keys())
        mas_costoso = max(list_carrito_compras_values)

        for i in range(len(list_carrito_compras_values)):
            if mas_costoso == list_carrito_compras_values[i]:
                dic_costoso = list_carrito_compras_keys[i]
                costoso.append(dic_costoso)
        
        if len(costoso) == 0:
            mas_costoso = costoso
        else:
            mas_costoso = min(costoso)
    else:
        mas_costoso = 'No hay productos en el carrito'

    return mas_costoso

carrito_compras = {'chocolatinas': 1300, 'bocadillos': 500, 'galletas': 700}
print(producto_mas_costoso(carrito_compras))

carrito_compras = {'bananos': 2400, 'chocolatinas': 4000, 'detergente': 4000}
print(producto_mas_costoso(carrito_compras))