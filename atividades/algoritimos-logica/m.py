""" Elaborar um programa que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados em uma matriz A de uma dimensão para 10 elementos. Apresentar os valores armazenados na matriz. """

matriz_A = []

num = float(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    matriz_A.append(i*num)

x = 1
print("Tabuada:")
for resultado in matriz_A:
    print(f"{num} * {x} = {resultado}")
    x += 1