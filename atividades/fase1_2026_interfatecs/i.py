n , k = map(int, input().split())
soma_total = 0
if n >= 1 and n <= 100 and k>= 1 and k <= 100:

    for i in range(1, n+1):
        soma_total = i + soma_total

    if soma_total % k == 0:
        print("POSSIVEL")
    else:
        print("IMPOSSIVEL")