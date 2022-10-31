import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def combinar_imagenes(rojo, verde, azul):
    img_rojo = mpimg.imread(rojo)
    img_verde = mpimg.imread(verde)
    img_azul = mpimg.imread(azul)

    componente_rojo = img_rojo[:, :, 0]
    componente_verde = img_verde[:, :, 1]
    componente_azul = img_azul[:, :, 2]

    rgb = np.dstack((componente_rojo, componente_verde, componente_azul))

    return rgb