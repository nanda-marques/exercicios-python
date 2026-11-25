n, k = map(int, input().split())
i = 0
mce = 0
if n >= 1 and n <=100 and k >= 1 and k <=1140:
    while i < n:
        c, m = map(int, input().split())
        mce = ((c * k) + m) + mce
        i += 1

print(f"Relatorio MCE: {mce} minutos de esforço total")
