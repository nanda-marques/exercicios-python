novamente = str("s")
score_p1 = 0
score_p2 = 0

while novamente == "s":
    p1 = input("Jogador 1: ")
    p2 = input("Jogador 2: ")
    if p1 == p2:
        print("Empate!")
    elif (p1 == "pedra") & (p2 == "tesoura") or (p1 == "tesoura") & (p2 == "papel") or (p1 == "papel") & (p2 == "pedra"):
        print("O jogador 1 é o vencedor!")
        score_p1 += 1
    elif (p2 == "pedra") & (p1 == "tesoura") or (p2 == "tesoura") & (p1 == "papel") or (p2 == "papel") & (p1 == "pedra"):
        print("O jogador 2 é o vencedor!")
        score_p2 += 1
    else:
        print("Rodada inválida! Houve um erro de digitação.")

    print(f"Placar: {score_p1} x {score_p2}")

    novamente = input("Deseja jogar novamente? (s/n): ")

print("\nFim de Jogo!")
print(f"Placar final: {score_p1} x {score_p2}")