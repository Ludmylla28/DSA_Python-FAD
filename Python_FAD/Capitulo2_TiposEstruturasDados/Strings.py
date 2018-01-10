#Para executar no terminal: python nome_arquivo.py

print("Criando uma string")
print("------------------")
# Uma única palavra
print('Olá')
# Uma frase
print('Isto é uma string em Python')
# Podemos usar aspas duplas
print("Isto é uma string em Python, usando aspas duplas")
# Você pode combinar aspas duplas e simples
print("Testando strings em 'Python'")

print("\nImprimindo uma String")
print("---------------------")
print ('Testando Strings em Python')
print("\n")
print ('Testando \nStrings \nem \nPython')
print ('\n')

print("Indexando Strings")
print("-----------------")
# Atribuindo uma string
s = 'Data Science Academy'
print(s)
# Primeiro elemento da string.
print(s[0])
print(s[1])
print(s[2])
print("\n")
# Retorna todos os elementos da string, começando pela posição (lembre que Python começa a indexação pela posição 0),
# até o fim da string.
print(s[1:])
# A string original permanece inalterada
print(s)
# Retorna tudo até a posição 3
print(s[:3])
print(s[:])
# Nós também podemos usar a indexação negativa e ler de trás para frente.
print(s[-1])
# Retornar tudo, exceto a última letra
print(s[:-1])
"""
Nós também podemos usar a notação de índice e fatiar a string em pedaços específicos (o padrão é 1). 
Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica 
a frequência para retornar elementos. Por exemplo:
"""
print(s[::1])
print(s[::2])
print(s[::-1])

print("\nPropriedades de Strings")
print("-----------------------")
print(s)
# Concatenando strings
print(s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!')
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
print(s)
# Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'
print('\n' + letra * 3)

print("\nFunções Built-in de Strings")
print("---------------------------")
print(s)
# Upper Case
print(s.upper())
# Lower case
print(s.lower())
# Dividir uma string por espaços em branco (padrão)
print(s.split())
# Dividir uma string por um elemento específico
print(s.split('y'))

print("\nFunções String")
print("--------------")
s = 'olá! seja bem vindo ao universo de python'
print(s.capitalize())
print(s.count('a'))
print(s.find('p'))
print(s.center(20, 'z'))
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.endswith('o'))
print(s.partition('!'))

print("\nComparando Strings")
print("------------------")
print("Python" == "R")
print("Python" == "Python")
