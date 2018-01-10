print("Metodos Especiais")
print("-----------------")
# Criando a classe Livro
class Livro(object):
    def __init__(self, titulo, autor, paginas):
        print ("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Título: %s , autor: %s, páginas: %s " \
    %(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816)

# Métodos especiais
print(livro1)

print(str(livro1))
print(len(livro1))

# Ao executar a função del para remover um atributo, o Python executa:
# livro1.__delattr__("paginas")
del livro1.paginas
print(hasattr(livro1, "paginas"))
