from collections import Counter

S = input().strip()
V = int(input().strip())

# tokens iniciais: cada caractere
tokens = list(S)
vocab = set(tokens)

while len(vocab) < V:
    # gerar todos os trios consecutivos
    trios = [tuple(tokens[i:i+3]) for i in range(len(tokens) - 2)]
    if not trios:
        break

    # contar frequências com Counter
    freq = Counter(trios)
    mais_freq = max(freq.values())

    # se nenhum trio aparece mais de uma vez e há mais de um trio, parar
    if mais_freq == 1 and len(freq) > 1:
        break

    # escolher o trio mais frequente (desempate por ordem alfabética)
    candidatos = [t for t, c in freq.items() if c == mais_freq]
    escolhido = min(candidatos)

    # novo token
    novo_token = ''.join(escolhido)

    # substituir todas as ocorrências do trio na sequência
    i = 0
    nova_seq = []
    while i < len(tokens):
        if i <= len(tokens) - 3 and tuple(tokens[i:i+3]) == escolhido:
            nova_seq.append(novo_token)
            i += 3
        else:
            nova_seq.append(tokens[i])
            i += 1

    tokens = nova_seq
    vocab.add(novo_token)

# imprimir resultado
print(' '.join(tokens))
