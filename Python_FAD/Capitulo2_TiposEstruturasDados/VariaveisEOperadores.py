#Para executar no terminal: python nome_arquivo.py

print("Variáveis e Operadores")
print("----------------------")

# Atribuindo o valor 1 à variável var_teste
var_teste = 1
# Imprimindo o valor da variável
var_teste
# Imprimindo o valor da variável
print(var_teste)

# Não podemos utilizar uma variável que não foi definida.
# my_var

var_teste = 2
var_teste
print(var_teste)
print(type(var_teste))

var_teste = 9.5
print(type(var_teste))

x = 1
print(x)

print("\nDeclaração múltipla")
print("-------------------")

pessoa1, pessoa2, pessoa3 = "Maria", "José", "Tobias"
print(pessoa1)
print(pessoa2)
print(pessoa3)
print("\n")
fruta1 = fruta2 = fruta3 = "Laranja"
print(fruta1)
print(fruta2)

print("\nVariáveis atribuídas a outras variáveis e ordem dos operadores")
print("--------------------------------------------------------------")
largura = 2
altura = 4
area = largura * altura
print(area)

perimetro = 2 * largura + 2 * altura
print(perimetro)
# A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2)  * altura
print(perimetro)

print("\nOperações com variáveis")
print("-----------------------")
idade1 = 25
idade2 = 35
print(idade1 + idade2)
print(idade2 - idade1)
print(idade2 * idade1)
print(idade2 / idade1)
print(idade2 % idade1)

print("\nConcatenação de variáveis")
print("-------------------------")
nome = "João"
sobrenome = "Zezinho"
fullName = nome + " " + sobrenome
print(fullName)