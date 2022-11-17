linhas = int(input("Digite quantas linhas tera a matriz?"))
colunas = int(input("Digite quantas colunas tera a matriz?"))
impares = []
listaValor = []


def criaMatriz(l, c):
    matriz = []
    for i in range(l):
        matriz.append(c * [0])
    return matriz


matriz = criaMatriz(linhas, colunas)
print(matriz)

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f"Digite um valor {[i], [j]}"))


def achaValores():
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            listaValor.append(valor)
            if valor % 2 != 0:
                impares.append(valor)


achaValores()

for i, valor in enumerate(matriz):
    print(valor)

print(f"A matriz possui {len(impares)} numeros impares!\nCom menor valor sendo {min(listaValor)}")
