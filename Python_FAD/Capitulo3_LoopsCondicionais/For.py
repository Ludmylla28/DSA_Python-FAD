print("Loop For")
print("--------")
# Criando uma tupla e imprimindo cada um dos valores
tupla = (2,3,4)
for i in tupla:
    print(i)
print("\n")
# Criando uma lista e imprimindo cada um dos valores
ListaDoMercado = ["Leite", "Frutas", "Carne"]
for i in ListaDoMercado:
    print(i)
print("\n")
# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for contador in range(0,5):
    print(contador)
print("\n")
# Imprimindo na tela os números pares da lista de números
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print (num)
print("\n")
# Listando os números no intervalo entre 0 e 101, com incremento em 2
for i in range(0,101,2):
    print(i)
print("\n")
# Strings também são sequências
for caracter in 'Python é uma linguagem de programação divertida!':
    print (caracter)
print("\n")

print("\nLoops Aninhados")
print("---------------")
# Loops aninhados
for i in range(0,5):
    for a in range(0,5):
        print(a)
print("\n")
# Operando os valores de uma lista com loop for
listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)
print("\n")
# Loops em lista de listas
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
for valor in listas:
    print(valor)
print("\n")
# Contando os itens de uma lista
lista = [5, 6, 10, 13, 17]
count = 0
for item in lista:
    count += 1

print(count)
print("\n")
# Contando o número de colunas
lst = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
primeira_linha = lst[0]
count = 0
for column in primeira_linha:
    count = count + 1

print(count)
print("\n")
# Pesquisando em listas
listaC = [5, 6, 7, 10, 50]

# Loop através da lista
for item in listaC:
    if item == 5:
        print("Número encontrado na lista!")
print("\n")
# Listando as chaves de um dicionário
dict = {'k1':'Python','k2':'R','k3':'Scala'}
for item in dict:
    print(item)
print("\n")
# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k,v in dict.items():
    print (k,v)
print("\n")