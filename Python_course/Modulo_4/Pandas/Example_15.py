import pandas as pd

a1 = {'tiempo' : 9.58, 'atleta' : 'Usain Bolt', 'pais' : 'Jamaica', 'fecha' : '16/08/2009', 'ciudad' : 'Berlin'}
a2 = {'tiempo' : 9.69, 'atleta' : 'Usain Bolt', 'pais' : 'Jamaica', 'fecha' : '16/09/2009', 'ciudad' : 'Beijing'}
a3 = {'tiempo' : 9.72, 'atleta' : 'Usain Bolt', 'pais' : 'Jamaica', 'fecha' : '31/05/2009', 'ciudad' : 'New York'}
a4 = {'tiempo' : 9.74, 'atleta' : 'Asafa Powell', 'pais' : 'Jamaica', 'fecha' : '9/09/2009', 'ciudad' : 'Rieti'}
a5 = {'tiempo' : 9.77, 'atleta' : 'Asafa Powell', 'pais' : 'Jamaica', 'fecha' : '18/08/2009', 'ciudad' : 'Zurich'}

records = [a1, a2, a3, a4, a5]

df_records1 = pd.DataFrame(records)

tiempos = [9.58, 9.69, 9.72, 9.74, 9.77]
atletas = ['Usain Bolt', 'Usain Bolt', 'Usain Bolt', 'Asafa Powell', 'Asafa Powell']
paises = ['Jamaica', 'Jamaica', 'Jamaica', 'Jamaica', 'Jamaica']
fechas = ['16/08/2009', '16/09/2009', '31/05/2009', '9/09/2009', '18/08/2009']
ciudades = ['Berlin', 'Beijing', 'New York', 'Rieti', 'Zurich']

datos = {'tiempo' : tiempos, 'atleta' : atletas, 'pais' : paises, 'fecha' : fechas, 'ciudad' : ciudades}

df_records2 = pd.DataFrame(datos)

tiempos = pd.Series([9.58, 9.69, 9.72, 9.74, 9.77])
atletas = pd.Series(['Usain Bolt', 'Usain Bolt', 'Usain Bolt', 'Asafa Powell', 'Asafa Powell'])
paises = pd.Series(['Jamaica', 'Jamaica', 'Jamaica', 'Jamaica', 'Jamaica'])
fechas = pd.Series(['16/08/2009', '16/09/2009', '31/05/2009', '9/09/2009', '18/08/2009'])
ciudades = pd.Series(['Berlin', 'Beijing', 'New York', 'Rieti', 'Zurich'])

datos_series = {'tiempo' : tiempos, 'atleta' : atletas, 'pais' : paises, 'fecha' : fechas, 'ciudad' : ciudades}

df_records3 = pd.DataFrame(datos_series)

df_records4 = pd.read_csv('datos_estado_test.csv')
df_records4.columns
columnas_valores = ['Observação', 'Data', 'Mês', 'Ano - Safra']
valores = df_records4[columnas_valores].copy()
print(valores)