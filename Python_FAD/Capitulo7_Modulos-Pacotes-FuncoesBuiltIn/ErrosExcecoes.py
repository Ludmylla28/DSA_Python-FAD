print("Erros e Exceções")
print("----------------")
# Erro
print('Olá)
# Criando uma função
def numDiv (num1, num2):
    resultado = num1 / num2
    print(resultado)
# Execução não gera erro
print(numDiv(4,2))
# Execução gerando erro
numDiv(4,0)

print("\nTry, Except, Finally")
print("--------------------")
8 + 's'
# Utilizando try e except
try:
    8 + 's'
except TypeError:
    print("Operação não permitida")
# Utilizando try, except e else
try:
    f = open('testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()
# Utilizando try, except e else
try:
    f = open('testandoerros','r')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()

 try:
    f = open('testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()
finally:
   print ("Comandos no bloco finally são sempre executados!")

def askint():
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
        finally:
            print ("Obrigado!")
        print (val)
print(askint())

def askint():
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            val = int(input("Tente novamente. Digite um número: "))
        finally:
            print ("Obrigado!")
        print (val)
print(askint())

def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val)
print(askint())

tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print('Erro: ', e)
except IOError as e:
    print('Erro de I/O:', e)

# Uma lista completa de exceções em Python, pode ser encontrada aqui:
# https://docs.python.org/3.6/library/exceptions.html
