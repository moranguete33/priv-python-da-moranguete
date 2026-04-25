import pandas as pd

# Ler planilha Excel
df = pd.read_excel("dados_funcionarios.xlsx")

# Agrupar por registro e nome
resultado = df.groupby(["Registro", "Nome"])["Horas"].sum()

# mostrando o resultado

for (registro, nome), horas in resultado.items():
    print(f"{registro} - {nome} - {horas} horas")
    