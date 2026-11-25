class Pilha:
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

s = Pilha()

print(s.isEmpty())

s.push(4)
s.push('Dog')
print(s.peek())

s.push(True)

print(s.size())
print(s.isEmpty())

s.push(8.4)
print(s.pop())
print(s.pop())

print(s.size())