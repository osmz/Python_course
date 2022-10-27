# Construya una función que reciba dos vectores (con 3 componentes cada uno) y retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada vector debe recibirse como una tupla con tres valores flotantes.

def suma_vectorial(vector_1, vector_2):
    x1 , y1 , z1 = vector_1
    x2 , y2 , z2 = vector_2

    x3 = x1 + x2
    y3 = y1 + y2
    z3 = z1 + z2
    
    vector_3 = (x3, y3, z3)

    return vector_3