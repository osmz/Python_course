# Función que recibe por parámetro cuatro números enteros y va a retornar el mayor de estos, teniendo en cuenta que si hay dos o más mayores, puede retornar cualquiera. 
# Es decir, si tenemos los números 3, 5, 5 y 2, nuestra función puede retornar el primer 5 o el segundo 5 de manera indiferente. 

def mayor_v1(a, b, c, d):
    mayor = a;
    if (b > mayor):
        mayor = b;
    if (c > mayor):
        mayor = c;
    if (d > mayor):
        mayor = d;
    
    return print(mayor)

mayor_v1(8, 12, 32, 5)