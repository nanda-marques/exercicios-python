#  Ler 10 elementos de uma matriz tipo vetor e apresentá-los.
matriz = []
for i in range(0, 10):
    num = (int(input(f"Digite o {i+1}º número: ")))
    matriz.insert(i, num)

    i += 1

print(matriz)