# Este ejercicio consiste en llevar los valores de una matriz que  representa una imagen a dos colores: negro y blanco. En cada posición de  la matriz que representa la imagen, hay una tupla de 3 flotantes entre 0 y 1 que representan los valores R, G y B del píxel. 

# Para ello, se establece un umbral (valor entre 0 y 1) y los  píxeles con promedio de color que  son iguales o mayores al  umbral se cambian a blanco (todos los valores de la tupla en 1) y los que están por  debajo se cambian a negro (todos los valores de la tupla en 0).

import cv2
import matplotlib.pyplot as plt

def binarizar_imagen(imagen, umbral):
    nueva_imagen = []
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        fila_nueva = []
        for j in range(ancho):
            promedio = (sum(imagen[i][j]) / 3)

            if promedio >= umbral:
                tupla = ( 1, 1, 1)
            else:
                tupla = ( 0, 0, 0)
            
            fila_nueva.append(tupla)
        nueva_imagen.append(fila_nueva)

    plt.imshow(nueva_imagen)
    plt.axis('off')
    #plt.savefig('test-filtro')
    plt.show()

    return nueva_imagen

imagen = cv2.imread('Imagen_test.jpg')
cv2.imshow('imagen', imagen)
cv2.waitKey()
umbral = 1
print(binarizar_imagen(imagen, umbral))