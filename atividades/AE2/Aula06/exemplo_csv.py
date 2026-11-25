import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [28, 34, 22],
    "cidade": ["São Paulo", "Curitiba", "Belo Horizonte"],
}

df = pd.DataFrame(dados)
df.to_csv("pessoas.csv", index=False, encoding="utf-8")
