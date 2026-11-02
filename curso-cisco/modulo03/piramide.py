blocks = int(input("Insira o número de blocos:"))  

altura = 0
while blocks > 0:
    altura += 1
    blocks -= altura
    print(" " * (altura - 1) + "*" * (altura * 2 - 1))
print("A altura da pirâmide:", altura)