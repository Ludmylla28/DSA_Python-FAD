print("Módulos e Pacotes")
print("-----------------")
# Bibilioteca Padrão

# Importando um módulo em Python
import math
# Verificando todos os métodos disponíveis no módulo
dir(math)
# Usando um dos métodos do módulo math
print(math.sqrt(25))
# Importando apenas um dos métodos do módulo math
from math import sqrt
# Usando o método
print(sqrt(9))
# Imprimindo todos os métodos do módulo math
print(dir(math))
# Help do método sqrt do módulo math
# help(sqrt)

import random
print(random.choice(['Maça', 'Banana', 'Laranja']))
print(random.sample(range(100), 10))

import statistics
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados))
print(statistics.median(dados))

import os
print(os.getcwd())
print(dir(os))

import sys
print(sys.stdout.write('Teste'))
print(sys.version)
print(dir(sys))

# Importando o módulo request do pacote urllib, usado para trazer url's
# para dentro do nosso ambiente Python
import urllib.request
# Variável resposta armazena o objeto de conexão à url passada como
# parâmetro
resposta = urllib.request.urlopen('http://python.org')
# Objeto resposta
print(resposta)
# Chamando o método read() do objeto resposta e armazenando o código
# html na variável html
html = resposta.read()
# Imprimindo html
print(html)

# Importando o arquivo com a cotação das ações da Petrobras, lendo o
# arquivo com o Pandas e gerando um gráfico com Matplotlib
from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas
# %matplotlib inline

endereco = 'http://real-chart.finance.yahoo.com/table.csv?s=PETR4.SA&d=9&e=17&f=2015&g=d&a=0&b=3&c=2000&ignore=.csv'
arquivo = urlopen(endereco)

petrobras = pandas.read_csv(arquivo, index_col=0, parse_dates=True)
petrobras.plot(y='Adj Close')

plt.xlabel('Ano')
plt.ylabel('Cotação')
plt.legend().set_visible(False)
print(plt.show())

import pandas
import pandas as pd
from pandas import DataFrame

print(petrobras.head())
df = pd.DataFrame(petrobras)
print(df)
