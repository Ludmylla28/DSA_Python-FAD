#Para executar no terminal: python nome_arquivo.py

print("Listas")
print("------")
# Criando uma lista
listadomercado = ["ovos, farinha, leite, maças"]
# Imprimindo a lista
print(listadomercado)
# Criando outra lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]
# Imprimindo a lista
print(listadomercado2)
# Criando lista
lista3 = [12, 100, "Universidade"]
# Imprimindo
print(lista3)
lista3 = [12, 100, "Universidade"]
# Atribuindo cada valor da lista a uma variável.
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]
# Imprimindo as variáveis
print(item1, item2, item3)

print("\nAtualizando um item da lista")
print("----------------------------")
# Imprimindo um item da lista
print(listadomercado2[2])
# Atualizando um item da lista
listadomercado2[2] = "chocolate"
# Imprimindo lista alterada
print(listadomercado2)

print("\nDeletando um item da lista")
print("--------------------------")
# Out of index. Não é possível deletar um item que não existe na lista
# del listadomercado2[4]

# Deletando um item específico da lista
del listadomercado2[3]
# Imprimindo o item com a lista alterada
print(listadomercado2)

print("\nListas de listas (Listas aninhadas")
print("----------------------------------")
# Criando uma lista de listas
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
# Imprimindo a lista
print(listas)
# Atribuindo um item da lista a uma variável
a = listas[0]
print(a)
b = a[0]
print(b)
list1 = listas[1]
print(list1)
valor_1_0 = list1[0]
print(valor_1_0)
valor_1_2 = list1[2]
print(valor_1_2)
list2 = listas[2]
print(list2)
valor_2_0 = list2[0]
print(valor_2_0)

print("\nOperações com listas")
print("--------------------")
# Criando uma lista aninhada (lista de listas)
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print(listas)
# Atribuindo à variável a, o primeiro valor da primeira lista
a = listas[0][0]
print(a)
b = listas[1][2]
print(b)
c = listas[0][2] + 10
print(c)
d = 10
print(d)
e = d * listas[2][0]
print(e)

print("\nConcatenando listas")
print("-------------------")
lista_s1 = [34, 32, 56]
print(lista_s1)
lista_s2 = [21, 90, 51]
print(lista_s2)
# Concatenando listas
lista_total = lista_s1 + lista_s2
print(lista_total)

print("\nOperador in")
print("-----------")
# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]
# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)
# Verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)

print("\nFunções Built-in")
print("----------------")
# Função len() retorna o comprimento da lista
print(len(lista_teste_op))
# Função max() retorna o valor máximo da lista
print(max(lista_teste_op))
# Função min() retorna o valor mínimo da lista
print(min(lista_teste_op))

# Criando uma lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]
# Adicionando um item à lista
listadomercado2.append("carne")
print(listadomercado2)
listadomercado2.append("carne")
print(listadomercado2)
print(listadomercado2.count("carne"))

# Criando uma lista vazia
a = []
print(a)
print(type(a))
a.append(10)
print(a)
a.append(50)
print(a)
old_list = [1,2,5,10]
new_list = []
# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)

print(new_list)

c = [20,30]
c.append(60)
c.append(70)
print(c)
print(c.count(20))

cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)
print(cidades.index('Salvador'))
# print(cidades.index('Rio de Janeiro'))
print(cidades)
cidades.insert(2, 110)
print(cidades)
# Remove um item da lista
cidades.remove(110)
print(cidades)
# Reverte a lista
cidades.reverse()
# Imprime a lista
print(cidades)

x = [3, 4, 2, 1]
print(x)
# Ordena a lista
x.sort()
print(x)