import random

dado = [1, 2, 3, 4, 5, 6]
jogador1 = []
jogador2 = []
jogada = 1


def menu():
    print("[MENU]\nSelecione as opcoes:\n[1] - Jogar\n[2] - Sair")
    escolha = int(input("sua escolha:"))
    if escolha == 1:
        return jogo()
    if escolha == 2:
        return score()


def randomLista():
    return random.choice(dado)


def jogo():
    global jogada
    num = randomLista()
    if jogada % 2 != 0:
        jogador1.append(num)
        print(f"Jogador 1 jogou {num}.")
        jogada += 1
    else:
        jogador2.append(num)
        print(f"Jogador 2 jogou {num}")
        jogada += 1
    jogarNovamente()


def score():
    print(
        f"Jogadas do jogador1: {jogador1}\nJogadas do jogador2: {jogador2}\nSoma jogador1: {sum(jogador1)}\nSoma jogador2: {sum(jogador2)}")
    if sum(jogador1) > sum(jogador2):
        print("O jogador 1 venceu !\nValeu !")
    if sum(jogador1) == sum(jogador2):
        print("Empate !")
    if sum(jogador1) < sum(jogador2):
        print("Jogador 2 venceu !\nValeu !")


def jogarNovamente():
    print("o que fazer?\n[1] proxima jogada\n[2] menu")
    escolha = int(input(":"))
    match escolha:
        case 1:
            jogo()
        case 2:
            menu()


menu()



