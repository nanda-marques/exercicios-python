# Processamento Recursivo de Dados Salariais
# Algoritmos e Estrutura de Dados II

# Profº Romulo
# Fernanda Marques

import pandas as pd


# Geração do Arquivo de Dados (Setup)

setup = {
    'nome': ['Fernanda', 'Manu', 'Matheus', 'Thiago', 'Felipe', 'Lucas', 'Mayra', 'Mayara', 'Alessandra', 'Marilene'],
    'salario': [2000.00, 1000.00, 1500.00, 2500.00, 4000.00, 6000.00, 1800.00, 950.90, 3200.00, 8000.00]
}

df = pd.DataFrame(setup)
df.to_csv('salarios.csv', index=False, encoding="utf-8")

# Implementação da Recursividade

""" 
Implementação da Recursividade:

Crie uma função recursiva principal que receba a lista de salários (extraída do CSV) e uma estrutura de dados (uma lista Python atuando como pilha) como argumentos.

Essa função recursiva deve iterar sobre os salários da lista de entrada (reduzindo a lista a cada passo) e realizar as seguintes ações:

Cálculo da Soma Total:

A função recursiva deve calcular e retornar a soma total de todos os salários contidos no arquivo CSV. O valor acumulado deve ser passado como um argumento na chamada recursiva.
"""

salarios = pd.read_csv('salarios.csv')
print(salarios.columns)

coluna_salario = salarios['salario']

# classe base copiada da atividade 02 
class Salarios:
    def __init__(self):
        self.itens = []

    def isEmpty(self):
        return self.itens == []

    def push(self, item):
        self.itens.append(item)   
        
    def pop(self):
        return self.itens.pop()

    def peek(self):
        return self.itens[len(self.itens)-1]
    
    def size(self):
        return len(self.itens)

def principal(coluna_salario, itens, soma):
        pass

# coluna_salario é a coluna extraída do csv 
# itens precisa ser mais bem definido, o que ele representa?
# soma é um acumulador dos valores dos salários