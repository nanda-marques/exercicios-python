# Nó (Node) da lista encadeada
# Cada nó contém um valor (dado) e uma referência para o próximo nó na lista.
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# Lista Encadeada
# Contém métodos para inserir, remover e exibir elementos da lista.
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        # cabeça é o primeiro nó da lista, inicialmente None (vazio)

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca 
        self.cabeca = novo_no

    def remover(self, valor):
        atual = self.cabeca
        anterior = None

        while atual and atual.dado != valor:
            anterior = atual
            atual = atual.proximo

            if not atual:
                return False
            if anterior:
                anterior.proximo = atual.proximo
            else: 
                self.cabeca = atual.proximo
                return True
            
    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

# Exemplo de uso da lista encadeada
lista = ListaEncadeada()
lista.inserir_inicio(3)
lista.inserir_inicio(5)
lista.inserir_inicio(7)
lista.exibir()  

lista.remover(5)
lista.exibir()