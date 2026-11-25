""" Ler três matrizes (A, B e C) de uma dimensão com 5 elementos cada. Construir uma matriz D, sendo esta a junção das três outras matrizes. Desta forma D deverá ter o triplo de elementos, ou seja, 15. Apresentar os elementos da matriz D. """

matriz_A = []
matriz_B = []
matriz_C = []

print("\nMatriz A:")
for i in range(5):
    i += 1
    matriz_A.append(int(input(f"Digite o {i}º valor: ")))

print("\nMatriz B:")
for i in range(5):
    i += 1
    matriz_B.append(int(input(f"Digite o {i}º valor: ")))

print("\nMatriz C:")
for i in range(5):
    i += 1
    matriz_C.append(int(input(f"Digite o {i}º valor: ")))

matriz_D = matriz_A + matriz_B + matriz_C

print(f"Eis a junção das matrizes A, B e C: {matriz_D}")