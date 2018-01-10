print("Objetos")
print("-------")
# Criando uma lista
lst_num = [1, 2, 3]
# A lista lst_num é um objeto, uma instância da classe lista em Python
print(type(lst_num))
print("\n")
# Usamos a função type, para verificar o tipo de um objeto
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))
print("\n")

# Criando um novo tipo de objeto chamado Carro
class Carro(object):
    pass
# Instância do Carro
palio = Carro()
print(type(palio))
print("\n")

# Criando uma classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("João", 12, 9.5)
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
print(Estudante1.nome)
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
print(Estudante1.idade)
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
print(Estudante1.nota)
print("\n")

# Criando uma classe
class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def listFunc(self):
        print("O nome do funcionário é " + self.nome + " e o salário é R$" + str(self.salario))

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Func1 = Funcionarios("Obama", 20000)
# Usando o método da classe
print(Func1.listFunc())

print("**** Usando atributos *****")
print(hasattr(Func1, "nome"))
print(hasattr(Func1, "salario"))
setattr(Func1, "salario", 4500)
print(hasattr(Func1, "salario"))
print(getattr(Func1, "salario"))
delattr(Func1, "salario")
print(hasattr(Func1, "salario"))