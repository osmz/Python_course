# En matemáticas, la sucesión o serie de Fibonacci es la siguiente sucesión infinita de números naturales: 0,1,1,2,3,5,8,13,...

# La sucesión comienza con los números 0 y 1, y a partir de estos, cada término es la suma de los dos anteriores.

# Cree una función que reciba un número que indica la cantidad de números de la sucesión que se quieren encontrar y retorne una cadena con los números separados por coma.

# Por ejemplo, el resultado de la función, si se pasa como parámetro el número 18 es el siguiente:

# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597

def sucesion_fibonacci(cantidad_numeros):
    a = 0
    b = 1
    list =[0,1]
    if cantidad_numeros == 1:
        s = str(list[0])
    elif cantidad_numeros == 2:
        s = ','.join([str(i) for i in list])
    else:
        for i in range(cantidad_numeros-2):
            c = a + b
            s = list.append(c)
            s = ','.join([str(i) for i in list])
            a = b
            b = c               

    return s    
        
print(sucesion_fibonacci(1))
