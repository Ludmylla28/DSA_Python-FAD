print("Expressões Regulares")
print("--------------------")
# Importando o módulo re (regular expression)
# Esse módulo fornece operações com expressões regulares (ER)
import re
# Lista de termos para busca
lista_pesquisa = ['informações', 'Negócios']
# Text to parse
texto = 'Existem muitos desafios para o Big Data. O primeiro deles é a coleta dos dados, pois fala-se aqui de '\
'enormes quantidades sendo geradas em uma taxa maior do que um servidor comum seria capaz de processar e armazenar. '\
'O segundo desafio é justamente o de processar essas informações. Com elas então distribuídas, a aplicação deve ser '\
'capaz de consumir partes das informações e gerar pequenas quantidades de dados processados, que serão calculados em '\
'conjunto depois para criar o resultado final. Outro desafio é a exibição dos resultados, de forma que as informações '\
'estejam disponíveis de forma clara para os tomadores de decisão.'
# Exemplo básico de Data Mining
for item in lista_pesquisa:
    print ('Buscando por "%s" em: \n\n"%s"' % (item, texto))

    # Verificando se o termo de pesquisa existe no texto
    if re.search(item,  texto):
        print ('\n')
        print ('Palavra encontrada. \n')
        print ('\n')
    else:
        print ('\n')
        print ('Palavra não encontrada.')
        print ('\n')
# Termo usado para dividir uma string
split_term = '@'
frase = 'Qual o domínio de alguém com o e-mail: aluno@gmail.com'
# Dividindo a frase
re.split(split_term, frase)

def encontra_padrao(lista, frase):

    for item in lista:
        print ('Pesquisando na frase: %r' %item)
        print (re.findall(item, frase))
        print ('\n')

frase_padrao = 'zLzL..zzzLLL...zLLLzLLL...LzLz...dzzzzz...zLLLL'

lista_padroes = [ 'zL*',       # z seguido de zero ou mais L
                  'zL+',       # z seguido por um ou mais L
                  'zL?',       # z seguido por zero ou um L
                  'zL{3}',     # z seguido por três L
                  'zL{2,3}',   # z seguido por dois a três L
                ]

encontra_padrao(lista_padroes, frase_padrao)

frase = 'Esta é uma string com pontuação. Isso pode ser um problema quando fazemos mineração de dados em busca '\
        'de padrões! Não seria melhor retirar os sinais ao fim de cada frase?'

# A expressão [^!.? ] verifica por valores que não sejam pontuação
# (!, ., ?) e o sinal de adição (+) verifica se o item aparece pelo menos
# uma vez. Traduzindo: esta expressão diz: traga apenas as palavras na
# frase.
re.findall('[^!.? ]+', frase)

frase = 'Esta é uma frase de exemplo. Vamos verificar quais padrões serão encontrados.'

lista_padroes = [ '[a-z]+',      # sequência de letras minúsculas
                  '[A-Z]+',      # sequência de letras maiúsculas
                  '[a-zA-Z]+',   # sequência de letras minúsculas e maiúsculas
                  '[A-Z][a-z]+'] # uma letra maiúscula, seguida de uma letra minúscula

encontra_padrao(lista_padroes, frase)

print("\nEscape Codes")
print("------------")
# O prefixo r antes da expressão regular evita o pré-processamento da ER
# pela linguagem. Colocamos o modificador r (do inglês "raw", crú)
# imediatamente antes das aspas
r'\b'
'\b'

frase = 'Esta é uma string com alguns números, como 1287 e um símbolo #hashtag'

lista_padroes = [ r'\d+', # sequência de dígitos
                  r'\D+', # sequência de não-dígitos
                  r'\s+', # sequência de espaços
                  r'\S+', # sequência de não-espaços
                  r'\w+', # caracteres alfanuméricos
                  r'\W+', # não-alfanumérico
                ]

encontra_padrao(lista_padroes, frase)
