M = [[1,0,0], [0,1,0], [0,0,1]]
print(M[-1][0])
print(M[-1][-1])
print('-')

for i in range(0,3):
    print(M[i])

print('-')

for i in range(0,3):
    for j in range(0,3):
        print(M[i][j])

# Segundo ejemplo

M = [[1,0,0], [0,1,0], [0,0,1]]
s = 0

for i in range(0,3):
    for j in range(0,3):
        s += M[i][j]
        print(s)

print(s/9)

# Tercer ejemplo

n = int(input('Ingrese el tamaño de la matriz identidad: '))

M = []
i = 0

while i < n:
    fila_nueva = [0] * n
    fila_nueva[i] = 1
    M.append(fila_nueva)
    i += 1

for fila in M:
    print(fila)