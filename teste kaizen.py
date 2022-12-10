import pandas as pd

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 200)

df = pd.read_csv('dados.csv', sep=';')

#Utilize a coluna 'Codigo' como índice
df = df.set_index('Codigo')

#Quantos produtos distintos temos?
proddist = []

for i in range(0, len(df['Produto'])):
    if df['Produto'][i] not in proddist:
        proddist.append(df['Produto'][i])

print(f"São {len(proddist)} produtos distintos.")

maiorvol = 0

for i in range(0 , len(df['Produto'])):
    volume = df['Altura'][i]*df['Largura'][i]*df['Profundidade'][i]
    if volume > maiorvol:
        maiorvol = volume
        maiorvolprod = df['Produto'][i]

print(f"O maior volume é {maiorvolprod}")



