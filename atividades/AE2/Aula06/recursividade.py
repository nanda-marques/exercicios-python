# Uma função que chama a si mesma

def contagem_regressiva(n):
    if n == 0:  # caso base
        print("Fim!")

    else: 
        print(n)
        contagem_regressiva(n-1) # passo recursivo

print("\nContagem regressiva:")
contagem_regressiva(5)

def fatorial(n):
    if n == 0 or n == 1: # caso base
        return 1
    return n * fatorial(n-1) # passo recursivo
print("\nFatorial: ")
print(fatorial(5))

# Recursivo:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print("\nFibonacci Recursivo:")
print(fibonacci(6))

# Iterativo

def fibonacci_iterativo(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b
    return a

print("\nFibonacci Iterativo:")
print(fibonacci_iterativo(6))  # 8​

# Potência
def potencia(base, exp):

    if exp == 0:  # Caso base​
        return 1
    return base * potencia(base, exp - 1)

print("\nPotência: (2^5)")
print(potencia(2, 5))  # 32​

# Soma de uma lista
def soma_lista(lista):
    if not lista:  # Caso base: lista vazia​
        return 0

    return lista[0] + soma_lista(lista[1:])

print("\nSoma de uma lista ([1, 2, 3, 4, 5]): ")
print(soma_lista([1, 2, 3, 4, 5]))  # 15​

# ATIVIDADE
# Usando recursividade: soma de elementos menores que 50

""" Iteração 
def soma_menores(n):
    soma = 0
    while n < 50:
        soma = n + soma
        n = n + 1
    return soma """

def soma_menores(n, soma = 1):
    if n > 50:  # caso base (condição de parada)
        return soma
    else:
        soma += n
        n += 1
        return soma_menores(n, soma) # recursividaede

print("\nExercício - SOMA DOS NÚMEROS < 50: ")
print(soma_menores(0))
