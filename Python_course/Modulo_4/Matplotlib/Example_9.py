import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
tem_Bogota = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]
preci_Bogota = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]

plt.figure()
plt.plot(meses, tem_Bogota)

plt.figure(figsize = (7,4))
plt.plot(meses, tem_Bogota, label = 'Temperaturas')
plt.xlabel('Meses')
plt.ylabel('Temperatura')
plt.title('Temperatura promedio en Bogotá, por mes (1970 - 2000)')
plt.legend()

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.6])
ax.plot(meses, tem_Bogota, label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura')
ax.set_title('Temperatura promedio en Bogotá, por mes (1970 - 2000)')
ax.legend()

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.6])
ax.plot(meses, tem_Bogota, label = 'Temperaturas')
ax.plot(meses, preci_Bogota, label = 'Precipitación')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura')
ax.set_title('Temperatura promedio en Bogotá, por mes (1970 - 2000)')
ax.legend()

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.6])
ax.plot(meses, tem_Bogota, 'r', label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura', color = 'red')
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, 'b', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = 'blue')

plt.show()