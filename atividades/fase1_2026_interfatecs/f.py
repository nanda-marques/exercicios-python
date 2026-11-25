n, r = map(int, input().split()) # n -> num tipos de serviço; r -> qtd papel (metros)
x = 0
comprimento_total = 0
valor_total = 0
valor_falso = 0
if n >= 1 and n <=100 and r >= 1 and r <=100:
    r = r * 100

    while x < n:
        desc, qtd, v = map(str, input().split())
        qtd = int(qtd)
        v = float(v)

        if qtd >= 1 and qtd <=1000 and v >= 1 and v <=1000:

            a, b = desc.split('x')
            a = int(a)
            b = int(b)
            if a == 10:
                comprimento = b
            else:
                comprimento = a

            for foto in range(qtd):
                valor_falso += v
                if comprimento_total < r:
                    comprimento_total += comprimento 
                    if comprimento_total <= r:
                        valor_total += v 
            x +=1     
if valor_falso > valor_total:
    print(f"PARCIAL {int(valor_total)}")

if valor_falso == valor_total:
    print(f"COMPLETO {int(valor_total)}")
