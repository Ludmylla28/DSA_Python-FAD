print("Funções")
print("-------")
# Definindo uma função com parâmetro
def primeiraFunc(nome):
    print('Olá %s' %(nome))

primeiraFunc('Aluno')
print("\n")

def funcLeitura():
    for i in range(0, 5):
        print("Número " + str(i))

funcLeitura()
print("\n")

# Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
# Chamando a função e passando parâmetros
addNum(45, 3)

print("\nVariáveis locais e globais")
print("--------------------------")
# Variável Global
var_global = 10  # Esta é uma variável global
def multiply(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiply(10, 23)
print(var_global)
print("\n")

# Variável Local
var_global = 10
def multiply(num1, num2):
    var_local = num1 * num2
    print(var_local)

multiply(10, 23)
#print(var_local)

print("\nFunções Built-in")
print("----------------")
print(abs(-56))
print(abs(23))
print(bool(0))
print(bool(1))
print("\n")
# Criando um string
Frase = "Eu estou aprendendo Python"
# Tipo de variável Frase
print(type(Frase))
print("\n")
# Função dir() retorna o que funções podem ser usadas com um determinado objeto
dir(Frase)
print("\n")
# Função help() mostra para que serve o método que pode ser usado com o objeto
help(Frase.upper)
print("\n")
help(Frase.replace)

print("\nFunções str, int, float")
print("-----------------------")
# Erro ao executar por causa da conversão
"""
idade = input("Digite sua idade: ")
if idade > 13:
  print("Você pode acessar o Facebook")
"""
# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
  print("Você pode acessar o Facebook")
print("\n")

print(int("26"))
print(float("123.345"))
print(str(14))
print(len([23,34,45,46]))
array = ['a', 'b', 'c']
print(max(array))
print(min(array))
array = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
print(array)
print(max(array))
print(min(array))
list1 = [23, 23, 34, 45]
print(sum(list1))

print("\nCriando funções usando outras funções")
print("-------------------------------------")

import math

def numPrimo(num):
    '''
    Verificando se um número
    é primo.
    '''
    if (num % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

print(numPrimo(541))

print("\nFazendo split dos dados")
print("-----------------------")
# Fazendo split dos dados
def split_string(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados."
# Isso divide a string em uma lista.
print(split_string(texto))
# Podemos atribuir o output de uma função, para uma variável
token = split_string(texto)
print(token)

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"
def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)
print(lowercased_string)


# Funções com número variável de argumentos
def printVarInfo(arg1, *vartuple):
    # Imprimindo o valor do primeiro argumento
    print("O parâmetro passado foi: ", arg1)

    # Imprimindo o valor do segundo argumento
    for item in vartuple:
        print("O parâmetro passado foi: ", item)
    return;
# Fazendo chamada à função usando apenas 1 argumento
print(printVarInfo(10))
print(printVarInfo('Chocolate', 'Morango', 'Banana'))
