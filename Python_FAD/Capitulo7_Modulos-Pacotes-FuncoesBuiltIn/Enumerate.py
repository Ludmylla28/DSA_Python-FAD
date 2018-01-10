print("Enumerate")
print("---------")
# Criando uma lista
seq = ['a','b','c']
print(enumerate(seq))
print(list(enumerate(seq)))
print("\n")
# Imprimindo os valores de uma lista com a função enumerate() e
# seus respectivos índices
for indice, valor in enumerate(seq):
    print (indice, valor)
print("\n")

for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print (valor)
print("\n")

lista = ['Marketing', 'Tecnologia', 'Business']
for i, item in enumerate(lista):
    print(i, item)
print("\n")

for i, item in enumerate('Isso é uma string'):
    print(i, item)
print("\n")

for i, item in enumerate(range(10)):
    print(i, item)
