# Estrutura de Dados com Pandas

# 1. Introdução
# 2. Numpy vs Pandas
# 3. Séries (Colunas de um DataFrame)
# 4. DataFrames (Tabela de dados com linhas e colunas)

import pandas as pd

# Series
dados = [10,20,30,40,50,60]
serie = pd.Series(dados, index=['a','b','c','d', 'e','f'])

print(serie)
print(serie['a'])
print(serie.iloc[0])
print(serie + 10)

#DataFrame
dados = {
    'Nome': ['Alice', 'Gustavo', 'Sara'],
    'Idade': [22, 27, 24],
    'Bairro': ['Rocinha', 'Vila da Penha', 'Vista Alegra']
}
df = pd.DataFrame(dados)
print(df)
print(df.head(2))
print(df.tail(2))
print('=============================')
print(df['Nome'])
print('-----------------------------')
print(df.loc[0])
print('=============================')
df['Loucura'] = [12, 15, 45]
print(df)
print('-----------------------------')
df = df.drop('Loucura', axis=1)
print(df)
