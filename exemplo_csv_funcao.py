import pandas as pd

df = pd.read_csv('./teste.csv')

df_filtrado = df[df['estado'] == 'SP']

df_filtrado = df[df['data'] == '10/01/2024']


print(df_filtrado)



df2 = pd.read_csv('./teste2.csv')

df_filtrado2 = df2[df2['estado'] == 'RJ']

df_filtrado2 = df2[df2['data'] == '10/01/2024']

print(df_filtrado2)