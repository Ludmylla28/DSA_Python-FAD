print("Python e R")
print("----------")
# Instalar o pacote rpy2: pip install rpy2
# ou conca install rpy2

# Importando o rpy2
import rpy2.robjects as robjects
# Criando um objeto R com Python
obj = robjects.r['pi']
print(obj)
print(obj[0])
# Criando um função R a partir do Python
robjects.r('''
        rfunc <- function(x, verbose = FALSE) {
            if (verbose) {
                cat("Eu sou uma função em R.\n")
            }
            2 * pi * x
        }
        rfunc(3)
        ''')
# Imprimindo a definição da função
r_func = robjects.globalenv['rfunc']
print(r_func.r_repr())
# Fazendo chamada à função
res = r_func(4)
print(res)
# Fazendo chamada à função
res = r_func(4, 'TRUE')
print(res)

# Importando outros objetos do R
letras = robjects.r['letters']
rcode = 'paste(%s, collapse = "-")' %(letras.r_repr())
resultado = robjects.r(rcode)
print(resultado)
print(type(resultado))
# Criando um vetor de strings R no Python
vec_str = robjects.StrVector(['Python', 'e', 'R', 'juntos', 'só', 'na',
                              'Data Science Academy'])
print(vec_str.r_repr())
# Criando um vetor de inteiros R no Python
vec_int = robjects.IntVector([4, 5, 6])
print(vec_int.r_repr())
# Criando um vetor de floats R no Python
vec_flt = robjects.FloatVector([1.1, 2.2, 3.3])
print(vec_flt.r_repr())

# Matrizes R
vec = robjects.FloatVector([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
mat = robjects.r['matrix'](vec, nrow = 2)
print(mat)

# Chamando funções R
rsum = robjects.r['sum']
print(rsum(vec_int)[0])
print(type(rsum))

# Chamando funções R
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
r_rnorm = robjects.r['rnorm']
print(r_rnorm(100))
plt.hist(r_rnorm(100))

# Importando pacotes R
from rpy2.robjects.packages import importr
utils = importr("utils")
help_doc = utils.help("help")
print(help_doc[0])
str(help_doc)

print("\nExtensão R para o iPython")
print("-------------------------")
# Carregando extensões R
%load_ext rpy2.ipython
# Instalação de pacotes R
%R install.packages("plyr")
%R data(mtcars)
%Rpull mtcars

%%R
summary(mtcars)

mtcars.describe()

%R print(mean(mtcars$mpg))

%R vecx = c(1, 4, 5, 7); sd(vecx); mean(vecx)

%R vecy = c(2,4,3,9)

%R lm(formula = vecy ~ vecx)
%R plot(vecx, vecy)

# Código Python
import numpy as np
X = np.array([4.5,6.3,7.9])
X.mean()
# Código R
%Rpush X
%R mean(X)

# Convertendo um dataframe R para um dataframe Python
pd_df = mtcars
print(pd_df)
print(type(pd_df))

print("\nPlots")
print("-----")
import rpy2.robjects as robjects
r = robjects.r
x = robjects.IntVector(range(10))
y = r.rnorm(10)
print(r.X11())
# Criando uma matriz a partir de um vetor
r.layout(r.matrix(robjects.IntVector([1,2,3,2]), nrow = 2, ncol = 2))
# Gerando o gráfico
r.plot(r.runif(10), y, xlab = "Eixo x", ylab = "Eixo y", col = "red")

# Outro Exemplo - Principal Componente Analysis
from rpy2.robjects.packages import importr
graphics = importr('graphics')
grdevices = importr('grDevices')
base = importr('base')
stats = importr('stats')

import array

x = array.array('i', range(10))
y = stats.rnorm(10)

grdevices.X11()

graphics.par(mfrow = array.array('i', [2,2]))
graphics.plot(x, y, ylab = "Eixo y", col = "red")

kwargs = {'ylab':"Eixo y", 'type':"b", 'col':"blue", 'log':"x"}
graphics.plot(x, y, **kwargs)


m = base.matrix(stats.rnorm(100), ncol = 5)
pca = stats.princomp(m)
graphics.plot(pca, main = "Valores")
stats.biplot(pca, main = "biplot")

print("\nggplot")
print("------")
import numpy as np
import pandas as pd
import rpy2.robjects.packages as packages
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
# Importando o dataset do R, o mtcars
R = ro.r
datasets = packages.importr('datasets')
mtcars = packages.data(datasets).fetch('mtcars')['mtcars']
# Gerando o gráfico com ggplot
gp = ggplot2.ggplot(mtcars)
pyplot = (gp
      + ggplot2.aes_string(x = 'wt', y = 'mpg')
      + ggplot2.geom_point(ggplot2.aes_string(colour = 'qsec'))
      + ggplot2.scale_colour_gradient(low = "yellow", high = "red")
      + ggplot2.geom_smooth(method = 'auto')
      + ggplot2.labs(title = "mtcars", x = 'wt', y = 'mpg'))

pyplot.plot()

print("\nAnálise de Variância")
print("--------------------")
import rpy2.robjects as robjects

r = robjects.r

controle = robjects.FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,
                                 5.17,4.53,5.33,5.14])
tratamento = robjects.FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,
                                   6.03,4.89,4.32,4.69])

grupo = r.gl(2, 10, 20, labels = ["Controle","Tratamento"])
peso = controle + tratamento

robjects.globalenv["peso"] = peso
robjects.globalenv["grupo"] = grupo
lm_r = r.lm("peso ~ grupo")

# Imprimindo a análise
print(r.anova(lm_r))


lm_r = r.lm("peso ~ grupo - 1")
print(r.summary(lm_r))

print(lm_r.names)

# Imprimindo apenas os coeficientes
print(lm_r.rx2('coefficients'))
