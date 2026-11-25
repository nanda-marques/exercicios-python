""" Ler 20 elementos de uma matriz A tipo vetor e construir uma matriz B de mesma dimensão com os mesmos elementos da matriz A, sendo que deverão estar invertidos. Ou seja, o primeiro elemento de A passa a ser o último de B, o segundo elemento de A passa a ser o penúltimo de B e assim por diante. Apresentar as matrizes A e B.
 """

matriz_A = []
matriz_B = []

for i in range(0, 20):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_A.insert(i, num)

matriz_B = matriz_A[:]

matriz_B = matriz_B[::-1]

print("Matriz A")
print(matriz_A)

print("Matriz A invertida (Matriz B)")
print(matriz_B)
