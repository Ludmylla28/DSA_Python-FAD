print("NumPy")
print("-----")
# Importando o NumPy
import numpy as np

print("\nCriando Arrays")
print("--------------")
# Help
# help(np.array)

# Array criado a partir de uma lista:
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(vetor1)
# Um objeto do tipo ndarray é um recipiente multidimensional de itens
# do mesmo tipo e tamanho.
print(type(vetor1))
# Criando uma lista. Perceba como listas e arrays são objetos
# diferentes, com diferentes propriedades
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(lst)
print(type(lst))
# Imprimindo na tela um elemento específico no array
print(vetor1[0])
# Alterando um elemento do array
vetor1[0] = 100
print(vetor1)

# vetor1[0] = 'Novo elemento'

# Verificando o formato do array
print(vetor1.shape)

# A função arange cria um vetor contendo uma progressão aritmética
# a partir de um intervalo - start, stop, step
vetor2 = np.arange(0., 4.5, .5)
print(vetor2)
# Verificando o tipo do objeto
print(type(vetor2))
# Formato do array
print(np.shape(vetor2))
print(vetor2.dtype)

x = np.arange(1, 10, 0.25)
print(x)
print(np.zeros(10))
# Retorna 1 nas posições em diagonal e 0 no restante
z = np.eye(3)
print(z)
# Os valores passados como parâmetro, formam uma diagonal
d = np.diag(np.array([1, 2, 3, 4]))
print(d)
# Array de números complexos
c = np.array([1+2j, 3+4j, 5+6*1j])
print(c)
# Array de valores booleanos
b = np.array([True, False, False, True])
print(b)
# Array de strings
s = np.array(['Python', 'R', 'Julia'])
print(s)

# O método linspace (linearly spaced vector) retorna um número de
# valores igualmente distribuídos no intervalo especificado
print(np.linspace(0, 10))
print(np.linspace(0, 10, 15))
print(np.logspace(0, 5, 10))

print("\nCriando uma Matriz")
print("------------------")
# Criando uma matriz
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.shape)
# Criando uma matriz 2x3 apenas com números "1"
matriz1 = np.ones((2,3))
print(matriz1)
# Criando uma matriz a partir de uma lista de listas
lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]
# A função matrix cria uma matria a partir de uma sequência
matriz2 = np.matrix(lista)
print(matriz2)
print(type(matriz2))
# Formato da matriz
print(np.shape(matriz2))
print(matriz2.size)
print(matriz2.dtype)
print(matriz2.itemsize)
print(matriz2.nbytes)
print(matriz2[2,1])
# Alterando um elemento da matriz
matriz2[1,0] = 100
print(matriz2)

x = np.array([1, 2])  # NumPy decide o tipo dos dados
y = np.array([1.0, 2.0])  # NumPy decide o tipo dos dados
z = np.array([1, 2], dtype=np.float64)  # Forçamos um tipo dado em particular
print(x.dtype, y.dtype, z.dtype)

matriz3 = np.array([[24, 76], [35, 89]], dtype=float)
print(matriz3)
print(matriz3.itemsize)
print(matriz3.nbytes)
print(matriz3.ndim)
print(matriz3[1,1])
matriz3[1,1] = 100
print(matriz3)

print("\nUsando o método random() do NumPy")
print("-----------------------------------")
print(np.random.rand(10))

import matplotlib.pyplot as plt

# %matplotlib inline

print(np.random.rand(10))
plt.show((plt.hist(np.random.rand(1000))))

print(np.random.randn(5,5))
plt.show(plt.hist(np.random.randn(1000)))

imagem = np.random.rand(30, 30)
plt.imshow(imagem, cmap = plt.cm.hot)
plt.colorbar()

print("\nOperações com datasets")
print("----------------------")
import os
filename = os.path.join('iris.csv')

# No Windows use !more iris.csv. Mac ou Linux use !head iris.csv
# !head iris.csv

# Carregando um dataset para dentro de um array
arquivo = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)
print(arquivo)
print(type(arquivo))
# Gerando um plot a partir de um arquivo usando o NumPy
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
plt.show(plt.plot(var1, var2, 'o', markersize=8, alpha=0.75))

print("\nEstatística")
print("-----------")
# Criando um array
A = np.array([15, 23, 63, 94, 75])
# Em estatística a média é o valor que aponta para onde mais se
# concentram os dados de uma distribuição.
print(np.mean(A))
# O desvio padrão mostra o quanto de variação ou "dispersão" existe em
# relação à média (ou valor esperado).
# Um baixo desvio padrão indica que os dados tendem a estar próximos da
# média;
# Um desvio padrão alto indica que os dados estão espalhados por uma gama
# de valores
print(np.std(A))
# Variância de uma variável aleatória é uma medida da sua dispersão
# estatística, indicando "o quão longe" em geral os seus valores se
# encontram do valor esperado
print(np.var(A))

d = np.arange(1, 10)
print(d)
print(np.sum(d))
# Retorna o produto dos elementos
print(np.prod(d))
# Soma acumulada dos elementos
print(np.cumsum(d))

a = np.random.randn(400,2)
m = a.mean(0)
print(m, m.shape)

plt.plot(a[:,0], a[:,1], 'o', markersize=5, alpha=0.50)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()

print("\nOutras operações com arrays")
print("---------------------------")
# Slicing
a = np.diag(np.arange(3))
print(a)
print(a[1, 1])
print(a[1])

b = np.arange(10)
print(b)
# [start:end:step]
print(b[2:9:3])

# Comparação
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b)
print(np.array_equal(a, b))
print(a.min())
print(a.max())

# Somando um elemento ao array
print(np.array([1, 2, 3]) + 1.5)

# Usando o método around
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
b = np.around(a)
print(b)

# Criando um array
B = np.array([1, 2, 3, 4])
print(B)

# Copiando um array
C = B.flatten()
print(C)

# Criando um array
v = np.array([1, 2, 3])
# Adcionando uma dimensão ao array
print(v[:, np.newaxis], v[:,np.newaxis].shape, v[np.newaxis,:].shape)
# Repetindo os elementos de um array
print(np.repeat(v, 3))
# Repetindo os elementos de um array
print(np.tile(v, 3))

# Criando um array
w = np.array([5, 6])
# Concatenando
print(np.concatenate((v, w), axis=0))
# Copiando arrays
r = np.copy(v)
print(r)
