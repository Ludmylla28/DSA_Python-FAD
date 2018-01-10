print("Exercícios")
print("----------")

# Exercício 1 - Imprima na tela os números de 1 a 10
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ["obj1", "obj2", "obj3", "obj4", "obj5"]
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str1 = "Hello"
str2 = "World!"
str3 = str1 + " " + str2
print(str3)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5
# e depois utilize a função count do  objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(4))

# Exercício 5 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario = {'chave1':'valor1', 'chave2':'valor2', 'chave3':'valor3'}
print(dicionario)

# Exercício 6 - Adicione mais uma ferramenta ao dicionário criado no exercício anterior e imprima na tela
dicionario['chave4'] = 'valor4'
print(dicionario)

# Exercício 7 - Crie um arquivo chamado nomes.txt no diretório onde está este notebook, grave 5 nomes no arquivo e
# feche-o.
arq = open("nomes.txt", "w")
arq.write("Nome1 , Nome2, Nome3, Nome4, Nome5")
arq.close

# Exercício 8 - Abra o arquivo criado no item anterior e leia o arquivo na tela.
arq = open("nomes.txt", "r")
print(arq.read())

# Exercício 9 - Crie um dicionário vazio e imrpima na tela
dicionario2 = {}
print(dicionario2)

# Exercício 10 - Complelete o trecho de código abaixo criado com Pandas e use a função tail() para ler os últimos
# elementos do dataset.
import pandas as pd
file_name = "binary.csv"
df = pd.read_csv(file_name)

print(df.tail())