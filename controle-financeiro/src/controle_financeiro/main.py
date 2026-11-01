from time import gmtime, strftime

from .registros.registro import (
    login,
    cadastro,
    usuarios,
    nome,
    saldo,
    depositar,
    sacar
)

from .menus.menu import menu

def iniciar():
    print("Bem-vindo(a) ao sistema de controle financeiro!")
    print("Já possui cadastro?")

    p = input("s/n: ")

    if p == "s":
        if login(usuarios):
            principal()

    elif p == "n":
        if cadastro(usuarios):
            principal()

    else:
        print("Opção inválida")


def principal():
    print("")
    print("---------")
    print(strftime("%a, %d %b %Y", gmtime()))
    print(f"Bem-vindo(a), {nome()}!")
    print("")
    while True:
        opcao = menu()

        if opcao == "1":
            ver_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def depositar():
    pass


def sacar():
    pass


def ver_saldo():
    print(f"O saldo disponível é R${saldo()}")

iniciar()