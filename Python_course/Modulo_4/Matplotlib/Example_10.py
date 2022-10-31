import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
tem_Bogota = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]
preci_Bogota = [14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 15.0, 14.5, 14.7, 14.6, 14.2]

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(meses, tem_Bogota, 'r', label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura', color = 'red')
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, 'b', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = 'blue')

color_fondo = '#444444'
color_temp = '#FFAF5E'
color_prec = '#3399DC'

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 0.75, label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura', color = color_temp)
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.25, label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec)

color_fondo = '#444444'
color_temp = '#FFAF5E'
color_prec = '#3399DC'

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 2.15, linestyle = '--', label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura', color = color_temp)
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.55, ls = '-.', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec)

color_fondo = '#444444'
color_temp = '#FFAF5E'
color_prec = '#3399DC'

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 2.15, linestyle = '--', marker = 's', markersize = 6, markerfacecolor = 'red', label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura', color = color_temp)
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.55, ls = '-.', marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgewidth = 3, markeredgecolor = 'yellow', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec)

plt.show()
