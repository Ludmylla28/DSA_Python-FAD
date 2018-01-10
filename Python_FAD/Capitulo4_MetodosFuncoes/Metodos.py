print("Métodos")
print("-------")
# Criando uma lista
lst = [100, -2, 12, 65, 0]
# Usando um método do objeto lista
lst.append(10)
# Imprimindo a lista
print(lst)
# Usando um método do objeto lista
print(lst.count(10))
# A função help() explica como utilizar cada método de um objeto
help(lst.count)
# A função dir() mostra todos os métodos e atributos de um objeto
print(dir(lst))

a = 'Isso é uma string'
# O método de um objeto pode ser chamado dentro de uma função, como print()
print(a.split())
