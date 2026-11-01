# Atividade 1 - TAD - Classes e métodos
# Fernanda Marques - CDN - 2º Semestre 

import math 

class Circulo:
    def __init__(self):
        self.raio = 0

    def area(self):
        return math.pi*(self.raio**2) 

    def perimetro(self):
        return 2*math.pi*self.raio 

print("\n --- Círculo de raio = 5 --- \n")

exemplo = Circulo()

exemplo.raio = 5

print(f"A área do círculo é: {exemplo.area():.2f}")

print(f"O perímetro do círculo é: {exemplo.perimetro():.2f}")

print("\n --- Novo Círculo --- \n")

circle = Circulo()

circle.raio = float(input("Digite o valor do raio: "))

print(f"A área do círculo é: {circle.area():.2f}")

print(f"O perímetro do círculo é: {circle.perimetro():.2f}")