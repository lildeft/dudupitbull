size = int(input("Qual o tamanho da lista?"))


def criaLista(size):
    lista = [0] * size
    return lista

lista = criaLista(size)

for i in range(len(lista)):
    lista[i] = int(input(f"Digite o valor da posicao [{i}]:"))

listaReversa = list(reversed(lista))

print(f"Lista: {lista}\nLista reversa: {listaReversa}\nSoma dos valores da lista: {sum(lista)}\nO menor valor da lista:{min(lista)}")