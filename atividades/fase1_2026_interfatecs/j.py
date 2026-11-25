t, n = map(int, input().split()) # t -> tempo em horas; n -> qtd brinquedos
x = 0
tempo_total = 0
soma_notas = 0

if t >= 0 and t <= 100 and n>= 1 and n <= 1000:
    t_min = t * 60

    while x < n:
        s = input() # nome brinquedo

        if len(s) >= 1 and len(s) <= 100:

            i, d = map(int, input().split()) # i -> nota brinquedo; d -> duração (min)
            if i >= 0 and i <= 10 and d >= 0 and d <= 500:
                tempo_total += d
                soma_notas += i
        x += 1

    if tempo_total <= t_min:
        print(soma_notas)
    else:
        print(0)
    