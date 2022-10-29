# Queremos escribir una función que recibió una imagen, es decir, una matriz de tuplas, y una tupla con tres booleanos, donde cada uno de estos nos indica si se debe conservar el valor de cada componente RGB de cada píxel. Un "False" nos indica que ese componente debe quedar en cero. Por ejemplo, si el primer booleano es falso, nos dirá que tenemos que dejar en cero el componente rojo de todos los píxeles. Un "True" indicará lo contrario, y es que debe conservarse el valor del componente en el píxel. La función debe retornarnos una nueva imagen con el filtro aplicado

import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread('test.jpg')
cv2.imshow('imagen', imagen)
cv2.waitKey()

print(imagen)

def aplicar_filtro_color(imagen, conservar):
    nueva_imagen = []
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        fila_nueva = []
        for j in range(ancho):
            r,g,b = imagen[i][j]
            temp = [r,g,b]
            for k in range(3):
                if not conservar[k]:
                    temp[k] = 0
            nuevo_pixel = (temp[0], temp[1], temp[2])
            fila_nueva.append(nuevo_pixel)
        nueva_imagen.append(fila_nueva)

    plt.imshow(nueva_imagen)
    plt.axis('off')
    plt.savefig('test-filtro')
    plt.show()

    return nueva_imagen

#imagen = image. .open('test.jpg')
conservar = (1,0,1)
print(aplicar_filtro_color(imagen, conservar))



def convolucion_imagen(imagen, mascara):
    alto = len(imagen)
    ancho = len(imagen[0])

    tamano_mascara = len(mascara)
    div = int(tamano_mascara/2)

    imagen_nueva = imagen.copy()

    for i in range(alto):
        for j in range(ancho):
            suma_colores = [0.0, 0.0, 0.0]
            suma_coef_mascara = 0.0
            x = 0
            for fila in range(i-div, i+div+1):
                y = 0
                for columna in range(j-div, j+div+1):
                    if fila >=0 and fila < alto and columna >=0 and columna > ancho:
                        suma_colores[0] += (mascara[x][y] * imagen[fila][columna][0])
                        suma_colores[1] += (mascara[x][y] * imagen[fila][columna][1])
                        suma_colores[2] += (mascara[x][y] * imagen[fila][columna][2])
                        suma_coef_mascara += mascara[x][y]
                    y += 1
                x += 1
            if suma_coef_mascara != 0:
                nuevo_r = suma_colores[0] / suma_coef_mascara
                nuevo_g = suma_colores[1] / suma_coef_mascara
                nuevo_b = suma_colores[2] / suma_coef_mascara
            else:
                nuevo_r = suma_colores[0]
                nuevo_g = suma_colores[1]
                nuevo_b = suma_colores[2]
            
            nuevo_pixel = (nuevo_r, nuevo_g, nuevo_b)
            imagen_nueva[i][j] = nuevo_pixel
    
    return imagen_nueva


