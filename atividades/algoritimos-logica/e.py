""" Ler uma matriz A do tipo vetor com 15 elementos. Construir uma matriz B de mesmo tipo, sendo que cada elemento da matriz B seja o fatorial do elemento correspondente da matriz A. Apresentar as matrizes A e B. """

matriz_A = []
matriz_B = []

print("Matriz A:")
for i in range(0, 15):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_A.append(num)

    fatorial = 1

    while num > 1:
        fatorial = fatorial * num
        num -= 1
    matriz_B.append(fatorial)
    i += 1

print("Matriz A:")
print(matriz_A)

print("Matriz B:")
print(matriz_B)