print("Scikit-learn")
print("------------")
# Importando Matplotlib e Numpy
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

# Diâmetros (cm)
Diametros = [[7], [10], [15], [30], [45]]

# Preços (R$)
Precos = [[8], [11], [16], [38.5], [52]]

plt.figure()
plt.xlabel('Diâmetro(cm)')
plt.ylabel('Preço(R$)')
plt.title('Diâmetro x Preço')
plt.plot(Diametros, Precos, 'k.')
plt.axis([0, 60, 0, 60])
plt.grid(True)
plt.show()

# Importando o módulo de Regressão Linear do scikit-learn
from sklearn.linear_model import LinearRegression

# Preparando os dados de treino

# Vamos chamar de X os dados de diâmetro da Pizza.
X = [[7], [10], [15], [30], [45]]

# Vamos chamar de Y os dados de preço da Pizza.
Y = [[8], [11], [16], [38.5], [52]]

# Criando o modelo
modelo = LinearRegression()
print(type(modelo))
# Treinando o modelo
print(modelo.fit(X, Y))

# Prevendo o preço de uma pizza de 20 cm de diâmetro
print("Uma pizza de 20 cm de diâmetro deve custar: R$%.2f" % modelo.predict([20][0]))

print("\nConstruindo um scatter plot")
print("---------------------------")
# Coeficientes
print('Coeficiente: \n', modelo.coef_)

# MSE (mean square error)
print("MSE: %.2f" % np.mean((modelo.predict(X) - Y) ** 2))

# Score de variação: 1 representa predição perfeita
print('Score de variação: %.2f' % modelo.score(X, Y))

# Scatter Plot representando a regressão linear
plt.scatter(X, Y,  color = 'black')
plt.plot(X, modelo.predict(X), color = 'blue', linewidth = 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(())
plt.yticks(())

plt.show()

print("\nExplorando o Dataset Boston Housing")
print("-----------------------------------")
#Download: https://archive.ics.uci.edu/ml/datasets/Housing
# Importando os módulos necessários
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
#%matplotlib inline

# O dataset boston já está disponível no scikit-learn. Precisamos apenas carregá-lo.
from sklearn.datasets import load_boston
boston = load_boston()
# Verificando o tipo da variável boston
print(type(boston))
# Visualizando o shape do dataset, neste caso 506 instâncias (linhas) e 13 atributos (colunas)
print(boston.data.shape)
# Descrição do Dataset
print(boston.DESCR)
print(boston.feature_names)
# Convertendo o dataset em um DataFrame pandas
df = pd.DataFrame(boston.data)
print(df.head())
# Convertendo o título das colunas
df.columns = boston.feature_names
print(df.head())
# boston.target é uma array com o preço das casas
print(boston.target)
# Adicionando o preço da casa ao DataFrame
df['PRICE'] = boston.target
print(df.head())

print("\nPrevendo o preço das casas em Boston")
print("------------------------------------")
# Importando o módulo de regressão linear
from sklearn.linear_model import LinearRegression
# Não queremos o preço da casa como variável dependente
X = df.drop('PRICE', axis = 1)
# Definindo Y
Y = df.PRICE

plt.scatter(df.RM, Y)
plt.xlabel("Média do Número de Quartos por Casa (RM)")
plt.ylabel("Preço da Casa")
plt.title("Relação entre RM e Preço")
plt.show()

# Criando o objeto de regressão linear
regr = LinearRegression()
print(regr)
# Tipo do objeto
print(type(regr))
# Treinando o modelo
print(regr.fit(X, Y))
# Coeficientes
print("Coeficiente: ", regr.intercept_)
print("Número de Coeficiente: ", len(regr.coef_))
# Prevendo o preço da casa
print(regr.predict(X))

# Comparando preços originais x preços previstos
plt.scatter(df.PRICE, regr.predict(X))
plt.xlabel("Preço")
plt.ylabel("Preço Previsto")
plt.title("Preço Original x Preço Previsto")
plt.show()

print("\nErros na predição")
print("-----------------")
# Vamos calcular o MSE (Mean Squared Error)
mse1 = np.mean((df.PRICE - regr.predict(X)) ** 2)
print(mse1)
# Aplicando regressõa linear para apenas uma variável e calculando o MSE
regr = LinearRegression()
regr.fit(X[['PTRATIO']], df.PRICE)
mse2 = np.mean((df.PRICE - regr.predict(X[['PTRATIO']])) ** 2)
print(mse2)

# Dividindo X em dados de treino e de teste
X_treino = X[:-50]
X_teste = X[-50:]

# Dividindo Y em dados de treino e de teste
Y_treino = df.PRICE[:-50]
Y_teste = df.PRICE[-50:]

# Imprimindo o shape dos datasets
print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)

from sklearn.model_selection import train_test_split
# Dividindo X e Y em dados de treino e de teste
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, df.PRICE, test_size = 0.33, random_state = 5)
# Imprimindo o shape dos datasets
print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)
# Construindo um modelo de regressão
regr = LinearRegression()
# Treinando o modelo
regr.fit(X_treino, Y_treino)
# Definindo os dados de treino e teste
pred_treino = regr.predict(X_treino)
pred_teste = regr.predict(X_teste)
# Comparando preços originais x preços previstos
plt.scatter(regr.predict(X_treino), regr.predict(X_treino) - Y_treino, c = 'b', s = 40, alpha = 0.5)
plt.scatter(regr.predict(X_teste), regr.predict(X_teste) - Y_teste, c = 'g', s = 40, alpha = 0.5)
plt.hlines(y = 0, xmin = 0, xmax = 50)
plt.ylabel("Resíduo")
plt.title("Residual Plot - Treino(Azul), Teste(Verde)")
plt.show()
