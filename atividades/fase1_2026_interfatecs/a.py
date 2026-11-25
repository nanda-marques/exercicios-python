# float - H (1.0 ≤ H ≤ 1000.0) -> altura inicial

# float - F (0.0 < F < 1.0) -> fração da altura recuperada a cada salto

# int - N (1 ≤ N ≤ 100) -> último toque ao chão

h, f, n = map(float, input().split()) 
n = int(n)
altura = h
i = 1  

while i < n:
    h = (h * f) 
    altura += h * 2

    i += 1

print(f"Total distance: {altura}")