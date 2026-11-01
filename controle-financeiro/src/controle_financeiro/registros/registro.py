usuarios = {
        '123' : {
        'nome': 'fefe',
        'senha': '12',
        'saldo': 120
    }
}
saldo = 0

def cadastro(usuarios):
    print("")
    print("----- CADASTRO -----")

    nome = input("Digite seu nome: ").strip()
    cpf = input("Cadastre seu CPF: ").strip()
    senha = input("Cadastre sua senha: ").strip()

    usuarios[cpf] = {
        "nome": nome,
        "senha": senha,
        "saldo": saldo
    }
    print(usuarios[cpf]['nome'], "cadastrado(a) com sucesso!")
    return True, usuarios

def login(usuarios):
    print("")
    print("----- LOGIN -----")

    cpf = input("Digite seu CPF para entrar: ")
    senha = input("Digite sua senha: ")

    if cpf in usuarios:
        if senha == usuarios[cpf]["senha"]:
            return True
        else:
            print("Senha incorreta.")
            return False
    else:
        print("CPF não cadastrado.")
        print("Deseja realizar seu cadastro?")
        p = input("s/n: ")
        if p == "s":
            cadastro(usuarios)
            return True
        else:
            exit()
        return False

def nome():
    return usuarios['123'].get('nome')

def saldo():
    saldo = float(usuarios['123'].get('saldo'))
    
    return ("%.2f" % saldo)

def sacar():
    saque = float(input("Valor desejado: "))
    print(f"Valor inserido para sacar: {saque}")

    if saque > saldo:
        print("O valor desejado é maior que o disponível em sua conta, continuar tornará seu saldo negativo. Deseja continuar?")
        p = input("s/n: ")
        if p == 's':
            saldo = saque - saldo
        else:
            ""
def depositar(cpf):
    try:
        valor = float(input("Valor para depositar: R$ "))
    except ValueError:
        print("Digite um valor numérico válido.")
        return

    if valor <= 0:
        print("O depósito deve ser maior que zero.")
        return

    usuarios[cpf]["saldo"] += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
