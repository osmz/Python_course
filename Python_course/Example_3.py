# Example of functions

def fahrenheit_a_centigrados(grados_f):
    grados_cent = (grados_f - 32)*(5/9)
    return grados_cent

def centigrados_a_fahrenheit(grados_c):
    grados_f = (grados_c*9/5)+32
    return grados_f

def radianes_a_grados(radianes):
    pi = 3.14159
    return (360*radianes)/(2*pi)

def grados_a_radianes(grados):
    pi = 3.14159
    rad = (2*pi*grados)/360
    return rad

def invertir_numero(numero):
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    millares = numero % 10

    inverso = (unidades * 1000) + (decenas * 100) + (centenas *10) + millares

    return inverso

print(fahrenheit_a_centigrados(90))
print(centigrados_a_fahrenheit(20))
print(radianes_a_grados(20))
print(grados_a_radianes(45))
print(invertir_numero(3719))