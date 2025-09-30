# Manipulação de DataFrames

# Seleção de Dados no Pandas
# Filtro de Dados
# Agregação de Dados

import pandas as pd

# DataFrame
dados = {
    'Nome': ['Alice', 'Gustavo', 'Sara'],
    'Idade': [22, 27, 24],
    'Bairro': ['Rocinha', 'Vila da Penha', 'Vista Alegra']
}
df = pd.DataFrame(dados)

# Seleção de Dados
print('selecao de colunas')
print('===================================')

# -Seleção de Colunas
print(df['Nome'])
print(df[['Nome', 'Bairro', 'Idade']])

# -Seleção de Linhas
print('===================================')
print('selecao de linhas')
print('===================================')

# --Sleção de rótulos
print(df.loc[0])

# --Seleção de posição
print(df.iloc[0])


print('===================================')
print('alterando rotulos')
print('===================================')

indices = ['A1', 'A2', 'A3']
df = pd.DataFrame(dados, index=indices)
print(df)

print('===================================')
print('selecao de linhas com rotulos alterados')
print('===================================')

print(df.loc['A1', 'Nome'])

print('===================================')
print('selecao de multiplas linhas com rotulos alterados')
print('===================================')

print(df.loc[['A1', 'A3']])
print(df.loc['A1':'A3'])

# print('===================================')
# print('concatenacao')
# print('===================================')

# intervalo = pd.concat([df.loc['A1':'A3'], df.loc['A5':'A7']])
# print(intervalo)

## FILTROS
print('===================================')
print('Filtrando pela idade')
print('===================================')
print(df['Idade'] > 25)
dataframa_filtrado = df[df['Idade'] > 25]

# Mascara booleana
print('===================================')
print('dataframe_filtrado')
print('===================================')
print(dataframa_filtrado)

print('===================================')
print('Filtrando com combinacoes')
print('===================================')
filtro = (df['Idade']>25) & (df['Bairro'] == 'Vila da Penha') # Filtro com "e", ou seja, deve ter ambas as caracteristicas definidas
outro_df_filtrado = df[filtro]
print(outro_df_filtrado)

filtro = (df['Idade']>25) | (df['Bairro'] == 'Vista Alegre') # Filtro com "ou", ou seja, deve ter pelo menos 1 das caracteristicas definidas
outro_df_filtrado2 = df[filtro]
print(outro_df_filtrado2)

## Agregacao de Dados

print('===================================')
print('Agregacao de Dados')
print('===================================')
print(f"média de idade: {df['Idade'].mean()}")
print(f"soma das idades: {df['Idade'].sum()}")
print(f"soma das minumo: {df['Idade'].min()}")
print(f"soma das maximo: {df['Idade'].max()}")

print('===================================')
print('Media de idade por cidades')
print('===================================')
media_de_idade_por_bairro = df.groupby('Bairro')['Idade'].mean()
print(f"media das idades por cidade: {media_de_idade_por_bairro}")

