# Estrutura de Dados com Pandas

# 1. Introdução
# 2. Numpy vs Pandas
# 3. Séries (Colunas de um DataFrame)
# 4. DataFrames (Tabela de dados com linhas e colunas)

import pandas as pd

dados = [10,20,30,40,50,60]
serie = pd.Series(dados, index=['a','b','c','d', 'e','f'])

print(serie)
print(serie['a'])
print(serie.iloc[0])
print(serie + 10)

#DataFrame
dados = {
    'nome': ['Alice', 'Gustavo', 'Sara'],
    'idade': [22, 27, 24],
    'bairro': ['Rocinha', 'Vila da Penha', 'Vista Alegra']
}
df = pd.DataFrame(dados)
print(df)
print(df.head(2))
print(df.tail(2))
print('=============================')
print(df['nome'])
print('-----------------------------')
print(df.loc[0])
print('=============================')
df['Loucura'] = [12, 15, 45, 60, 70, 80, 100]
print(df)
print('-----------------------------')
df = df.drop('Loucura', axis=1)
print(df)
