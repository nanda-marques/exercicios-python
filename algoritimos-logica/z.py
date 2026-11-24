""" Ler uma matriz A de uma dimensão com 10 elementos numéricos inteiros. Apresentar o total de elementos ímpares existentes na matriz e também o percentual do valor total de números ímpares em relação à quantidade total de elementos armazenados na matriz."""

matriz_A = []

for i in range(10):
    i += 1
    matriz_A.append(int(input(f"Digite o {i}º numero: ")))

impares = 0
for num in matriz_A:
    if num % 2 != 0:
        impares += 1

percentual = (impares / len(matriz_A))*100

print(f"\nNa MATRIZ_A há {impares} números impares.")
print(f"Isso corresponde a {percentual}% da matriz A")