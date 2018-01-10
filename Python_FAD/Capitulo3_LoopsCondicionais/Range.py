print("Range")
print("-----")
# Imprimindo números pares entre 50 e 101
for i in range(50, 101, 2):
    print(i)
print("\n")

for i in range(3, 6):
    print (i)
print("\n")

for i in range(0, -20, -2):
    print(i)
print("\n")

lista = ['Morango', 'Banana', 'Maça', 'Uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i])
print("\n")

# Tudo em Python é um objeto
print(type(range(0,3)))