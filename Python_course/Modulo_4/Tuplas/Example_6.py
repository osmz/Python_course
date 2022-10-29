# En este ejercicio se debe reflejar la imagen verticalmente sobre una  línea imaginaria en el centro de la figura, creando una imagen espejo de  la figura original. En cada posición de la matriz que representa la  imagen hay una tupla de 3 flotantes entre 0 y 1 que representan los  valores R, G y B del píxel.

# Después de reflejar una figura, la distancia  entre la línea de reflexión y cada punto en la figura original es la  misma que la distancia entre la línea de reflexión y el punto  correspondiente en la imagen de espejo. Para hacer esta transformación,  se intercambian las columnas de píxeles de la imagen: La primera con la  última, la segunda con penúltima, etc.

import cv2
import matplotlib.pyplot as plt

def reflejar_imagen(imagen):
    matriz = imagen
    alto = len(matriz)
    ancho = len(matriz[0])
    for valor_eje_y in range(alto):
        for valor_eje_x in range(int(ancho/2)):
            indice_opuesto = ancho - valor_eje_x - 1
            opuesto = matriz[valor_eje_y][indice_opuesto]
            actual = matriz[valor_eje_y][valor_eje_x]
            matriz[valor_eje_y][indice_opuesto] = actual
            matriz[valor_eje_y][valor_eje_x] = opuesto

    plt.imshow(matriz)
    plt.axis('off')
    #plt.savefig('test-filtro')
    plt.show()

    return 'ok'

imagen = cv2.imread('Oscar1a.jpeg')
cv2.imshow('imagen', imagen)
cv2.waitKey()
print(reflejar_imagen(imagen))