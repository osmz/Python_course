import pandas as pd

datos = [19, 18, 29, 14, 20, 20, 20, 20, 19]
temperaturas = pd.Series(datos, name =  'Temperaturas de Bogotá')

datos = [19, 18, 29, 14, 20, 20, 20, 20, 19]
fechas = ['5/11/20', '6/11/20', '7/11/20', '8/11/20', '9/11/20', '10/11/20', '11/11/20', '12/11/20', '13/11/20']
temperaturas = pd.Series(datos, index = fechas, name =  'Temperaturas de Bogotá')

parejas = {'5/11/20': 19, '6/11/20' : 18, '7/11/20' : 29, '8/11/20' : 14, '9/11/20' : 20, '10/11/20' : 20, '11/11/20' : 20, '12/11/20' : 20, '13/11/20' : 19}
temperaturas = pd.Series(parejas)

temperaturas = temperaturas.reset_index(drop = True)

print(temperaturas)