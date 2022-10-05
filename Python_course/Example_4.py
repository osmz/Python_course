# Considere el software que se ejecuta en una máquina expendedora. Una de las tareas que debe realizar es determinar cuánto cambio debe entregarle al cliente luego de que paga. Escriba una función que recibe la cantidad de dinero (en pesos) a dar como cambio al cliente y retorne un mensaje con la cantidad de monedas de cada denominación que deben ser entregadas, teniendo en cuenta que el cambio se debe otorgar con la menor cantidad de monedas posible.

# La máquina cuenta con monedas de 500, 200, 100 y 50 pesos, y el cambio total se entregará con monedas de estas denominaciones. El mensaje retornado DEBE seguir el siguiente formato: “A,B,C,D” (sin espacios intermedios) donde A, B, C y D son la cantidad de monedas de 500, 200, 100 y 50, respectivamente.

def calcular_cambio(cambio):
    monedas_500 = cambio // 500
    monedas_200 = (cambio % 500) // 200
    monedas_100 = ((cambio % 500) % 200) // 100
    monedas_50 = (((cambio % 500) % 200) % 100)// 50
    mensaje = str(monedas_500) + "," + str(monedas_200) + "," + str(monedas_100)+ "," + str(monedas_50)
    return mensaje

print(calcular_cambio(6250))