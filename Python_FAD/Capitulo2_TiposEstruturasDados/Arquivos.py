print("Lendo arquivos")
print("--------------")
# Abrindo o arquivo para leitura
arq1 = open("arquivo-dsc.txt", "r")
# Lendo o arquivo
print(arq1.read())
# Contar o número de caracteres
print(arq1.tell())
# Retornar para o iníco do arquivo
print(arq1.seek(0,0))
# Ler os primeiros 10 caracteres
print(arq1.read(10))

print("\nGravando arquivos")
print("---------------")
# Abrindo arquivo para gravação
arq2 = open("arquivo-dsc.txt", "w")

# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura.
# print(arq2.read())

# Gravando arquivo
print(arq2.write("Testando gravação de arquivos em Python "))
arq2.close()
# Lendo arquivo gravado
arq2 = open("arquivo-dsc.txt", "r")
print(arq2.read())
# Acrescentando conteúdo
arq2 = open("arquivo-dsc.txt", "a")
print(arq2.write("Acrescentando conteúdo"))
arq2.close()
arq2 = open("arquivo-dsc.txt", "r")
print(arq2.read())
# Retornando ao início do arquivo para leitura
print(arq2.seek(0,0))
print(arq2.read())

print("\nAutomatizando o processo de gravação")
print("------------------------------------")
fileName = input("Digite o nome do arquivo: ") # Digite o nome do arquivo: teste
fileName = fileName + ".txt"
arq3 = open(fileName, "w")
print(arq3.write("Incluindo texto no arquivo criado"))
arq3.close()
arq3 = open(fileName, "r")
print(arq3.read())
arq3.close()

print("Abrindo um dataset em uma única linha")
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

print("\nContando as linhas de um arquivo")
print("--------------------------------")
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0
for row in full_data:
    count += 1   # Equivalente a: count = count + 1
print(count)

print("\nContando o número de colunas de um arquivo")
print("------------------------------------------")
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]

count = 0
for column in first_row:
    count = count + 1
print(count)

print("\nImportando um dataset com Pandas")
print("--------------------------------")
# Para importar o Pandas, antes deve-se instalá-lo usando o terminal
# através do comando: pip install pandas
# jgazal ~/PycharmProjects/Python_DSA $ pip install pandas
import pandas as pd
# file_name = "http://ats.ucla.edu/stat/data/binary.csv"
file_name = "binary.csv"
df = pd.read_csv(file_name)
print(df.head())

file2 = "salarios.csv"
df2 = pd.read_csv(file2)
print(df2.head())