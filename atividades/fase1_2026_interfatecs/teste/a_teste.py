tabela = { 1: 4, 2: 4.50, 3: 5, 4: 2, 5: 1.50 }

code, qtd = map(int, input().split())

print(f"Total: R$ {(tabela[code]*qtd):.2f}")