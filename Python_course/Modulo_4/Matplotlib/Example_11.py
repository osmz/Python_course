import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
tem_Bogota = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]
preci_Bogota = [40, 60, 80, 90, 100, 120, 40, 60, 80, 90, 100, 120]

color_fondo = '#444444'
color_temp = '#FFAF5E'
color_prec = '#3399DC'

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.grid(True)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 1.5, linestyle = '--', marker = 's', markersize = 6, markerfacecolor = 'red', label = 'Temperaturas')
ax.set_xlabel('Meses')
ax.set_ylabel('Temperatura', color = color_temp)
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.5, ls = '-.', marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgewidth = 3, markeredgecolor = 'yellow', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec)

color_fondo = '#444444'
color_temp = '#FFAF5E'
color_prec = '#3399DC'

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.grid(True)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 1.5, linestyle = '--', marker = 's', markersize = 6, markerfacecolor = 'red', label = 'Temperaturas')
ax.set_xlabel('Meses', style = 'italic', fontweight = 'bold')
ax.set_ylabel('Temperatura', color = color_temp, fontweight = 'bold')
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)', fontweight = 'bold')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.5, ls = '-.', marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgewidth = 3, markeredgecolor = 'yellow', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec, fontweight = 'bold')

color_fondo = '#444444'
color_temp = '#FFAF5E'
color_prec = '#3399DC'

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.grid(True)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 1.5, linestyle = '--', marker = 's', markersize = 6, markerfacecolor = 'red', label = 'Temperaturas')
ax.set_xlabel('Meses', style = 'italic', fontweight = 'bold')
ax.set_ylabel('Temperatura', color = color_temp, fontweight = 'bold')
for label in ax.get_yticklabels():
    label.set_color(color_temp)
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)', fontweight = 'bold')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.5, ls = '-.', marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgewidth = 3, markeredgecolor = 'yellow', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec, fontweight = 'bold')
for label in ax2.get_yticklabels():
    label.set_color(color_prec)

fig = plt.figure(figsize = (7,4))
#ax = fig.add_axes(['Izquierda, Abajo, Ancho, Alto'])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.set_alpha(0.9)
ax.grid(True)
ax.plot(meses, tem_Bogota, color = color_temp, linewidth = 1.5, linestyle = '--', marker = 's', markersize = 6, markerfacecolor = 'red', label = 'Temperaturas')
ax.set_xlabel('Meses', style = 'italic', fontweight = 'bold')
ax.set_ylabel('Temperatura', color = color_temp, fontweight = 'bold')
for label in ax.get_yticklabels():
    label.set_color(color_temp)
ax.set_ylim(10, 20)
ax.set_title('Temperatura y precipitación promedio en Bogotá, por mes (1970 - 2000)', fontweight = 'bold')
ax2 = ax.twinx()
ax2.plot(meses, preci_Bogota, color = color_prec, linewidth = 1.5, ls = '-.', marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgewidth = 3, markeredgecolor = 'yellow', label = 'Precipitación')
ax2.set_ylabel('Precipitación', color = color_prec, fontweight = 'bold')
for label in ax2.get_yticklabels():
    label.set_color(color_prec)
ax2.set_ylim(0, 200)

plt.show()