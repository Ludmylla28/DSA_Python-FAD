# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
# depois faça uma chamada à função para listar os números
def par():
    for i in range(2, 21, 2):
        print(i)

par()
print("\n")

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def frase(texto):
    print(texto.upper())
    return

frase('Rumo à Análise de Dados')
print("\n")

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista
def novaLista(lista):
    lista.append(5)
    lista.append(6)


lista1 = [1, 2, 3, 4]
novaLista(lista1)
print(lista1)
print("\n")

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def num(arg, *lista):
    print(arg)
    for i in lista:
        print (i)
    return;

# Chamada à função
num(1)
num('elm2', 'elm3', 'elm4')
print("\n")

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2
# números como parâmetro e retornar a soma deles
soma = lambda num1, num2: num1 + num2;
print ("Soma: ", soma(1122, 2017))
print("\n")

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0;
def soma( arg1, arg2 ):
    total = arg1 + arg2;
    print ("Dentro da função o total é : ", total)
    return total;

soma( 10, 20 );
print ("Fora da função o total é : ", total)
print("\n")

# Exercício 7 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd

file_name = "binary.csv"

def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()

print(retornaArq(file_name))