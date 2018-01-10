print("Herança")
print("-------")
# Criando a classe Animal
class Animal(object):
    def __init__(self):
        print("Animal criado")

    def Identif(self):
        print("Animal")

    def comer(self):
        print("Comendo")

# Criando a classe Cachorro
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")

    def Identif(self):
        print("Cachorro")

    def latir(self):
        print("Au Au!")

# Criando um objeto (Instanciando a classe)
puppy = Cachorro()
# Executando o método da classe Cachorro (sub classe)
puppy.Identif()
# Executando o método da classe Animal (super classe)
puppy.comer()
# Executando o método da classe Cachorro (sub classe)
puppy.latir()
