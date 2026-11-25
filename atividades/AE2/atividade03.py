# Fernanda Marques - CDN - 2º Semestre

# Exercício 1 - Criar Nó e Lista Encadeada com inserir_inicio, remover e exibir

class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self,dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def remover(self,valor):
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

# Exercício 2 - Comparar lista nativa com lista encadeada

lista_nativa = []
print(type(lista_nativa))

lista_nativa.insert(0, 3)
lista_nativa.insert(0, 5)
lista_nativa.insert(0, 1)
print("Lista Nativa:", lista_nativa)
lista_nativa.remove(5)
print("Lista Nativa:", lista_nativa)

for i in lista_nativa:
    print(i, end=" -> ")
print("None")

print("\nLista Encadeada:")
lista_encadeada = ListaEncadeada()

lista_encadeada.inserir_inicio(3)
lista_encadeada.inserir_inicio(5)
lista_encadeada.exibir()

# Enquanto a lista nativa é uma estrutura pronta do Python que tem métodos já estabelecidos, em que os índices são utilizados, como por exemplo: insert ou append para adicionar, remove ou pop para remover.
 
# A lista encadeada é uma estrutura que precisa ser implementada manualmente, ela é mais complexa, porém, mais flexível. Os índices não são usados. Para adicionar ou remover elementos criamos métodos como inserir_início e remover.