# Processamento Recursivo de Dados Salariais
# Algoritmos e Estrutura de Dados II

# Profº Romulo
# Fernanda Marques

import pandas as pd

# CRIA ARQUIVO CSV
setup = {
    'nome': ['Fernanda', 'Manu', 'Matheus', 'Thiago', 'Felipe', 'Lucas', 'Mayra', 'Mayara', 'Alessandra', 'Marilene'],
    'salario': [2000.00, 1000.00, 1500.00, 2500.00, 4000.00, 6000.00, 1800.00, 950.90, 3200.00, 8000.00]
}

# df = tabela com os dados; salvo em um arquivo CSV
df = pd.DataFrame(setup)
df.to_csv('salarios.csv', index=False, encoding="utf-8")


# LEITURA DOS DADOS
salarios = pd.read_csv('salarios.csv')

print("Nomes das colunas do csv:")
print(salarios.columns)

# Seleciona a coluna que contém os salários
coluna_salario = salarios['salario']

# CRIAÇÃO DA PILHA
class Salarios:
    def __init__(self):
        # Lista que armazena os salários
        self.itens = []

    def isEmpty(self):
        # Verifica se a pilha está vazia
        return self.itens == []

    def push(self, item):
        # Adiciona um salário ao topo da pilha
        self.itens.append(item)

    def pop(self):
        # Remove e retorna o último salário inserido
        return self.itens.pop()

    def peek(self):
        # Consulta o salário do topo sem removê-lo
        return self.itens[len(self.itens)-1]

# FUNÇÃO RECURSIVA
def principal(coluna_salario, itens, soma):

    # Caso base: encerra a recursão quando a lista fica vazia
    if len(coluna_salario) == 0:
        return soma

    # Pega o primeiro salário da lista
    salario_atual = coluna_salario[0]

    # Soma o salário atual ao valor acumulado
    soma += salario_atual

    # Adiciona o salário atual ao topo da pilha
    itens.push(salario_atual)

    # Chama a função novamente com os salários restantes
    return principal(coluna_salario[1:], itens, soma)

# LIFO
def ordenar_pilha(pilha):
    # Plha auxiliar 
    auxiliar = Salarios()

    # Continua enquanto houver salários na pilha original
    while not pilha.isEmpty():

        # Remove o salário do topo
        salario_atual = pilha.pop()

        # Devolve para a pilha original os valores maiores
        # até encontrar a posição correta do salário atual
        while not auxiliar.isEmpty() and auxiliar.peek() > salario_atual:
            pilha.push(auxiliar.pop())

        # Insere o salário na posição correta da pilha auxiliar
        auxiliar.push(salario_atual)

    # Retorna a pilha organizada
    return auxiliar

# EXECUÇÃO
# Pilha vazia que armazena os salários
pilha = Salarios()

# Converte a coluna em uma lista
lista_salarios = coluna_salario.tolist()

# Recursividade com lista, pilha e soma zerada
soma_total = principal(lista_salarios, pilha, 0)

print("Salários armazenados na pilha:", pilha.itens)

# Soma total calculada (função recursiva)
print(f"Soma total dos salários: R$ {soma_total:.2f}")

# Ordena os salários utilizando a pilha
pilha_ordenada = ordenar_pilha(pilha)

print("Salários em ordem crescente:", pilha_ordenada.itens)