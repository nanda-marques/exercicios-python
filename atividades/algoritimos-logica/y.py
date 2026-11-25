""" Ler uma matriz A de uma dimensão com 15 elementos numéricos inteiros. Apresentar o total de elementos pares existentes na matriz. """

matriz_A = []

for i in range(15):
    i += 1
    matriz_A.append(int(input(f"Digite o {i}º numero: ")))

pares = 0
for num in matriz_A:
    if num % 2 == 0:
        pares += 1

print(f"Na MATRIZ_A há {pares} números pares.")