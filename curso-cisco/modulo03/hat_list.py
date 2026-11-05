import os

hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

 # Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário. 
print(f"{hat_list}\n")

hat_list[2] = int(input("Digite um número para substituir o número do meio: "))

os.system('cls')

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.

print("\n O último elemento da lista será removido!")

print(".")
print("..")
print("...")
print("POP!")

hat_list.pop()
print(f"{hat_list}")

 # Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual
print(f"\n Eis o comprimento atual da lista: {len(hat_list)}")