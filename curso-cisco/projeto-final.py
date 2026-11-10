import random

# Jogo da Velha

# X = Computador
# O = Usuário

tabuleiro = [0, 1, 2, 3, "X", 5, 6, 7, 8]


def mostrar_tabuleiro():
    contador = 0

    for numero in tabuleiro:
        print(numero, end=" | ")
        contador += 1

        if contador == 3:
            print()
            print("-----------")
            contador = 0


def verificar_tabuleiro():

    # Linhas horizontais
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
        if tabuleiro[0] == "X":
            return "computador"
        elif tabuleiro[0] == "O":
            return "usuario"

    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
        if tabuleiro[3] == "X":
            return "computador"
        elif tabuleiro[3] == "O":
            return "usuario"

    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
        if tabuleiro[6] == "X":
            return "computador"
        elif tabuleiro[6] == "O":
            return "usuario"

    # Colunas verticais
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
        if tabuleiro[0] == "X":
            return "computador"
        elif tabuleiro[0] == "O":
            return "usuario"

    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        if tabuleiro[1] == "X":
            return "computador"
        elif tabuleiro[1] == "O":
            return "usuario"

    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        if tabuleiro[2] == "X":
            return "computador"
        elif tabuleiro[2] == "O":
            return "usuario"

    # Diagonais
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        if tabuleiro[0] == "X":
            return "computador"
        elif tabuleiro[0] == "O":
            return "usuario"

    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        if tabuleiro[2] == "X":
            return "computador"
        elif tabuleiro[2] == "O":
            return "usuario"

    # Verificar se ainda existem posições disponíveis
    for i in tabuleiro:
        if i != "X" and i != "O":
            return True

    return False


def jogada_computador():
    jogada = random.randint(0, 8)

    while tabuleiro[jogada] == "X" or tabuleiro[jogada] == "O":
        jogada = random.randint(0, 8)

    tabuleiro[jogada] = "X"
    mostrar_tabuleiro()

def jogada_usuario(posicao):
    mostrar_tabuleiro()
    while tabuleiro[posicao] == "X" or tabuleiro[posicao] == "O":
        print("Essa posição já foi ocupada! Digite novamente")
        mostrar_tabuleiro()
        posicao = int(input("Escolha uma posição para jogar: "))
    if tabuleiro[posicao] != "X" and tabuleiro[posicao] != "O":
        tabuleiro[posicao] = "O"
        mostrar_tabuleiro()

while verificar_tabuleiro() == True:
    posicao = int(input("Escolha uma posição para jogar: "))
    jogada_usuario(posicao)
    verificar_tabuleiro()
    jogada_computador()
    verificar_tabuleiro()



# Conferir o laço de jogadas while. Diferenciar vitórias da falta de espaço para novas jogadas.
# Começar a verificar o tabuleiro entre jogadas.

# As posições deveriam ser de 1 a 9.