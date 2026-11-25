""" Ler duas matrizes A e B do tipo vetor com 20 elementos. 
Construir uma matriz C, em que cada elemento de C é a subtração do elemento correspondente de A com B. 
Apresentar a matriz C. """

matriz_A = []
matriz_B = []
matriz_C = []

print("Matriz A:")
for i in range(0, 20):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_A.append(num)
    i += 1

print("Matriz B:")
for i in range(0, 20):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz_B.append(num)
    i += 1

for i in range(0, 20):
    matriz_C.append(matriz_A[i]-matriz_B[i])
    i += 1

print(matriz_C)