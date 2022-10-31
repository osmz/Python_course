# Implementar una función que nos permita convertir una imagen a negativo. Calcular el negativo de una imagen consiste en. El negativo de cada píxel que se obtiene restando uno; el valor máximo que puede tener un componente en la escala de Matplotlib; a cada componente RGB del píxel y tomar el valor absoluto de la diferencia. Con esos nuevos valores se crea el color negativo del píxel. Recordemos que como usaremos Matplotlib, debemos tener en cuenta que la imagen estará representada como una matriz de listas. Es decir, cada píxel será una lista de tamaño tres, donde cada valor representa uno de los componentes RGB, en vez de las duplas que habíamos manejado anteriormente.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def cargar_imagen(imagen):
    print('Calculando 1')
    imagen =  mpimg.imread(imagen).tolist()
    return imagen

def visualizar_imagen(imagen):
    print('Calculando 2')
    plt.imshow(imagen)
    plt.show()

def convertir_negativa(imagen):
    print('Calculando 3')
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            pixel = imagen[i][j]
            for k in range(3):
                imagen[i][j][k] = abs(pixel[k] - 1.0)
    
    return imagen

imagen = 'Oscar1a.jpeg'
def ejecutar(imagen):
    imagen1 = cargar_imagen(imagen)
    visualizar_imagen(imagen1)
    imagen2 = convertir_negativa(imagen1)
    visualizar_imagen(imagen2)

    return imagen2

print(ejecutar(imagen))