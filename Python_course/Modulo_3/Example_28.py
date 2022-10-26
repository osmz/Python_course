# Un matemático ha diseñado un juego muy sencillo para que sus hijos practiquen operaciones aritméticas básicas. En este juego, él les da una matriz cuadrada de más de 3x3 y les pide que "repinten la X" usando una operación determinada. Es decir, ellos tienen que devolver la matriz aplicando la operación sobre todas las casillas que hacen parte de las diagonales de la matriz.

# Las operaciones posibles son sumar, restar, multiplicar y dividir el valor de cada casilla por él mismo. Por ejemplo, si en una casilla de la X el número original era 5 y la operación que se debe aplicar es la suma, el valor 5 deberá reemplazarse por 10. 

# Construya una función que le sirva a los hijos del matemático para verificar sus respuestas. La función recibe una matriz cuadrada, una operación y retorna la matriz modificada según las reglas del juego.  

def pintar_x(matriz, operacion):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            valor1 = matriz[i][i]
            valor2 = matriz[i][-i-1]

        if operacion == '+':
            matriz[i][i] = valor1 + valor1
            matriz[i][-i-1] = valor2 + valor2
        
        if operacion == '-':
            matriz[i][i] = valor1 - valor1
            matriz[i][-i-1] = valor2 - valor2
        
        if operacion == '*':
            matriz[i][i] = valor1 * valor1
            matriz[i][-i-1] = valor2 * valor2
        
        if operacion == '/':
            matriz[i][i] = valor1 / valor1
            matriz[i][-i-1] = valor2 / valor2                

    return matriz    

matriz = [[1,2,3,0],
          [1,2,3,3],
          [5,7,3,2],
          [8,4,2,4]]
operacion = '+'

print(pintar_x(matriz, operacion))