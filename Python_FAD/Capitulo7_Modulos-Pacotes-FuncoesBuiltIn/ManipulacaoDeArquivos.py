print("Manipulação de Arquivos")
print("-----------------------")
print("Manipulando Arquivos TXT")
print("------------------------")
texto = "Cientista de Dados é a profissão que mais tem crescido ultimamente.\n"
texto = texto + "Esses profissionais precisam se especializar em Estatística, Programação e Machine Learning.\n"
texto += "E claro, em Big Data."
print(texto)
# Importando o módulo os
import os
# Criando um arquivo (no mesmo diretório onde está o Jupyter Notebook)
arquivo = open(os.path.join('cientista.txt'),'w')
# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra+' ')
# Fechando o arquivo
arquivo.close()
# !cat cientista.txt

# Lendo o arquivo
arquivo = open('cientista.txt','r')
texto = arquivo.read()
arquivo.close()
print (texto)

print("\nUsando a expressão with")
print("-----------------------")
with open('cientista.txt','r') as arquivo:
    texto = arquivo.read()
print(len(texto))
print(texto)
with open('cientista.txt','w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])
# !cat cientista.txt

print("\nManipulando Arquivos CSV (comma-separated values)")
print("-------------------------------------------------")
# Importando o módulo csv
import csv
with open('numeros.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira','segunda','terceira'))
    writer.writerow((55,93,76))
    writer.writerow((62,14,86))
# !cat numeros.csv

# Leitura de arquivos csv
with open('numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)
# Gerando uma lista com dados do arquivo csv
with open('numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
print (dados)
# Impriminfo a partir da segunda linha
for linha in dados[1:]:
    print (linha)

print("\nManipulando Arquivos JSON (Java Script Object Notation )")
print("--------------------------------------------------------")
# Criando um dicionário
dict = {'nome': 'Guido van Rossum',
        'linguagem': 'Python',
        'similar': ['c','Modula-3','lisp'],
        'users': 1000000}
for k,v in dict.items():
    print (k,v)
# Importando o módulo Json
import json
# Convertendo o dicionário para um objeto json
json.dumps(dict)
# Criando um arquivo Json
with open('dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))
# Leitura de arquivos Json
with open('dados.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print (data)
print (data['nome'])
# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]

print ('Título: ', data['title'])
print ('URL: ', data['url'])
print ('Duração: ', data['duration'])
print ('Número de Visualizações: ', data['stats_number_of_plays'])

# Copiando o conteúdo de um arquivo para outro
import os

arquivo_fonte = 'dados.json'
arquivo_destino = 'json_data.txt'

# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)
# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())
# !cat json_data.txt
