""" Ler 8 elementos em uma matriz A tipo vetor. Construir uma matriz B de
mesma dimensão com os elementos da matriz A multiplicados por 3. O
clemento B[1] deverá ser implicado pelo elemento A[1] * 3, o elemento
B[2] implicado pelo elemento A[2] * 3 e assim por diante, até 8. Apresentar
a matriz B. """

matriz_A = []
matriz_B = []

for i in range(0, 8):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_A.insert(i, num)
    matriz_B.append(matriz_A[i]*3)
    i += 1

print("Matriz B: ")
print(matriz_B)