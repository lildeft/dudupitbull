matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]


for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0


for i in range(5):
    print(matriz[i])