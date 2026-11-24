""" Ler duas matrizes A e B do tipo vetor com 15 elementos cada. Construir uma matriz C, sendo esta a junção das duas outras matrizes. Desta forma, C deverá ter o dobro de elementos, ou seja, 30. Apresentar a matriz C.
 """

matriz_A = []
matriz_B = []

print("Matriz A:")

for i in range(0, 15):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_A.append(num)

print("Matriz B:")

for i in range(0, 15):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_B.append(num)

matriz_C = matriz_A + matriz_B
print(matriz_C)