print("Pandas")
print("------")
print("\nSeries")
print("----")
from pandas import Series
import pandas as pd
# Criando uma série sem especificar os índices
Obj = Series([4, 7, -5, 3])
print(Obj)
print(type(Obj))
print(Obj.values)
print(Obj.index)

# Criando uma série e especificando os índices
Obj2 = Series([4, 7, -5, 3], index = ['a', 'b', 'c', 'd'])
print(Obj2)
print(Obj2.values)
print(Obj2.index)
print(Obj2[Obj2 > 3])
print(Obj2['b'])
print('d' in Obj2)

# Criando uma série de dados passando um dicionário como parâmetro
dict = {'Futebol':5200, 'Tenis': 120, 'Natação':698, 'Volleyball':1550}
# Criando uma série a partir de um dicionário
Obj3 = Series(dict)
print(Obj3)
print(type(Obj3))

# Criando uma lista
esportes = ['Futebol', 'Tenis', 'Natação', 'Basktetball']
# Criando uma serie e usando uma lista como índice
Obj4 = Series(dict, index=esportes)
print(Obj4)
print(pd.isnull(Obj4))
print(pd.notnull(Obj4))
print(Obj4.isnull())

# Concatenando Series
print(Obj3 + Obj4)

Obj4.name = 'população'
Obj4.index.name = 'esporte'
print(Obj4)

print("\nDataframes")
print("----------")
from pandas import DataFrame
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
print(type(frame))
print(DataFrame(data, columns=['Ano', 'Estado', 'População']))

frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'],
                   index = ['um', 'dois', 'três', 'quatro', 'cinco'])
# Imprimindo o Dataframe
print(frame2)
# Imprimindo apenas uma coluna do Dataframe
print(frame2['Estado'])
print(type(frame2))

print("\nUsando NumPy e Pandas")
print("---------------------")
# Importando o NumPy
import numpy as np
# Usando o NumpY para alimentar uma das colunas do dataframe
frame2['Débito'] = np.arange(5.)
print(frame2)
print(frame2.values)
# Resumo do Dataframe
print(frame2.describe())
# Tipos de dados no Dataframe
print(frame2.dtypes)
print(frame2.index)
print(frame2.columns)
print(frame2.values)
print(frame2['Ano'])
print(frame2.Ano)
print(frame2[:2])

# Criando um dicionário
web_stats = {'Dias':[1, 2, 3, 4, 5, 6, 7],
             'Visitantes':[45, 23, 67, 78, 23, 12, 14],
             'Taxas':[11, 22, 33, 44, 55, 66, 77]}
df = pd.DataFrame(web_stats)
print(df)
# Visualizando uma coluna  index
print(df.set_index('Dias'))
print(df.head())
print(df['Visitantes'])
print(df[['Visitantes', 'Taxas']])

print("\nLendo Arquivos csv")
print("------------------")
# Usando o método read_csv
df = pd.read_csv('salarios.csv')
print(df)
# Usando o método read_table
df = pd.read_table('salarios.csv', sep = ',')
print(df)

# No Windows use !type. No Mac ou Linux use !head
# !head salarios.csv
# pwd

# Alterando o título das colunas
df = pd.read_csv('salarios.csv', names = ['a', 'b', 'c', 'd'])
print(df)

import sys
data = pd.read_csv('salarios.csv')
print(data.to_csv(sys.stdout, sep = '|'))

# Criando um Dataframe
dates = pd.date_range('20130101', periods = 10)
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))
print(df)
print(df.head())
# quick data summary
print(df.describe())
# Calculando a média
print(df.mean())
# Pivot e cálculo da média
print(df.mean(1))
# Usando métodos
print(df.apply(np.cumsum))
# Merge de Dataframes
left = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna1': [1, 2]})
right = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna2': [4, 5]})
print(pd.merge(left, right, on='chave'))

# Adicionando um elemento ao Dataframe
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
s = df.iloc[3]
# Adicionando um elemento ao Dataframe
print(df.append(s, ignore_index=True))

print("\nTime Series")
print("-----------")
# Criando um range de datas com frequência de segundos
rng = pd.date_range('1/1/2016', periods = 50, freq = 'S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index = rng)
print(ts)
# Criando um range de datas com frequência de meses
rng = pd.date_range('1/1/2016', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)

print("\nPlotting")
print("--------")
import matplotlib.pyplot as plt
from matplotlib import style

#%matplotlib inline

# Time Series Plot
ts = pd.Series(np.random.randn(500), index=pd.date_range('1/1/2016', periods=500))
ts = ts.cumsum()
#ts.plot()
plt.show(ts.plot())

# DataFrame Plot
df = pd.DataFrame(np.random.randn(500, 4), index = ts.index, columns = ['A', 'B', 'C', 'D'])
df = df.cumsum()
#plt.figure(); df.plot(); plt.legend(loc = 'best')
plt.show(df.plot())

print("\nOutuput")
print("-------")
# import os
import os

# Verificando se o arquivo existe. No Windows use !type teste-df-output.xlsx
# !head teste-df-output.xlsx

# Gerando um arquivo excel a partir de um Dataframe
df.to_excel('teste-df-output.xlsx', sheet_name='Sheet1')

# Verificando se o arquivo existe. No Windows use !type teste-df-output.xlsx
# !head teste-df-output.xlsx

# Lendo o arquivo excel para um Dataframe
newDf2 = pd.read_excel('teste-df-output.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(newDf2.head())
os.remove('teste-df-output.xlsx')

# !head teste-df-output.xlsx
