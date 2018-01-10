print("Tuplas")
print("------")
# Criando uma tupla
tupla1 = ("Matemática", 23, "Gatos")
# Imprimindo a tupla
print(tupla1)

# Tuplas não suportam append()
# tupla1.append("Chocolate")

# Tuplas não suportam delete de um item específico
# del tupla1["Gatos"]

# Tuplas podem ter um único item
tupla1 = ("Chocolate")
print(tupla1)

tupla1 = ("Matemática", 23, "Gatos")
print(tupla1[0])
# Verificando o comprimento da tupla
print(len(tupla1))
# Slicing, da mesma forma que se faz com listas
print(tupla1[1:])
print(tupla1.index('Gatos'))

# Tuplas não suportam atribuição de item
# tupla1[1] = 21

# Deletando a tupla
del tupla1
# tupla1

# Criando uma tupla
t2 = ('A', 'B', 'C')
print(t2)
# Tuplas não suportam atribuição de item
# t2[0] = 'D'

# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)
print(lista_t2)
lista_t2.append('D')
# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)
print(t2)