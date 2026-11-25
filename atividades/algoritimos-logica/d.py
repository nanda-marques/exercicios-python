""" Ler 15 elementos de uma matriz A do tipo vetor. Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação: “Todo elemento de B deverá ser o quadrado do elemento de A correspondente”. Apresentar as matrizes A e B. """

matriz_A = []
matriz_B = []

print("Matriz A:")

for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    matriz_A.append(num)
    matriz_B.append(num ** 2)

print("Matriz A:")
print(matriz_A)

print("Matriz B:")
print(matriz_B)