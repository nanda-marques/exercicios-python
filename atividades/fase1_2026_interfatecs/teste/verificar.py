# -*- coding: utf-8 -*-

# Cédulas

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

n = int(input())

total = n // 100

print(f"{total} nota(s) de R$ 100,00") 
n = n - (total * 100) 
total = n // 50
print(f"{total} nota(s) de R$ 50,00") 
n = n - (total * 50) 
total = n // 20
print(f"{total} nota(s) de R$ 20,00") 
n = n - (total * 20) 
total = n // 10
print(f"{total} nota(s) de R$ 10,00") 
n = n - (total * 10) 
total = n // 5
print(f"{total} nota(s) de R$ 5,00") 
n = n - (total * 5) 
total = n // 2
print(f"{n // 2} nota(s) de R$ 2,00")
n = n - (total * 2) 
total = n // 1
print(f"{n // 1} nota(s) de R$ 1,00") 
