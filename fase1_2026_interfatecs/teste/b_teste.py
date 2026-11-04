h1, m1, h2, m2 = map(int, input().split())

total_inicio = (h1 * 60) + m1
total_fim = (h2 * 60) + m2

duracao_minutos = total_fim - total_inicio

# Se o tempo for menor ou igual a zero, significa que o jogo terminou no dia seguinte
if duracao_minutos <= 0:
    duracao_minutos += 24 * 60  # Adiciona 24 horas em minutos (1440 minutos)

hora = duracao_minutos // 60
minuto = duracao_minutos % 60

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")