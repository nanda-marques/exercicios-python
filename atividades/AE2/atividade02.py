# Atividade 2 - FIFO
# Fernanda Marques - CDN - 2º Semestre 

class Pacientes:
    def __init__(self):
        self.pacientes = []

    def vazio(self):
        return self.pacientes == []

    def push(self, novo):
        return self.pacientes.append(novo)

    def pop(self):
        return self.pacientes.pop()

    def peek(self):
        return self.pacientes[len(self.pacientes)-1]

    def size(self):
        return len(self.pacientes)

fila = Pacientes()

print("--- Teste ---")
print(f"Há pacientes na fila? \n - {fila.vazio()}")

print("--- Novos pacientes ---")
print(f"{fila.push("Fernanda")}")
print(f"{fila.push("Manuella")}")

print("--- Chamando o próximo paciente ---")
print(fila.pop())

print("--- Visualizando o próximo paciente ---")
print(fila.peek())

print("--- Teste ---")
print(f"Há pacientes na fila? {fila.vazio()}")

print("--- Quantos pacientes estão na fila? ---")
print(fila.size())