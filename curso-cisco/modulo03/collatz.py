# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode ser descrita da seguinte forma:

# pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
# se for par, avalie um novo c0 como c0 ÷ 2;
# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# se c0 ≠ 1 , volte ao ponto 2.
# A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.

num = int(input("Digite um número: "))
i = 0
if num != 0:
    c0 = num

    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = (c0 * 3) + 1
        print(int(c0))
        i += 1

print("Etapas: ", i)

