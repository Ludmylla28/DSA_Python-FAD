print("Seaborn")
print("-------")
# Para instalar: pip install seaborn
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sea
# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")
print(dados.head())
#Regressão linear é uma equação para se estimar a condicional (valor esperado)
# de uma variável y, dados os valores de algumas outras variáveis x.

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
# sea.jointplot("total_bill", "tip", dados, kind = 'reg');
plt.show(sea.jointplot("total_bill", "tip", dados, kind = 'reg'))
# O método lmplot() cria plot com dados e modelos de regressão.
#sea.lmplot("total_bill", "tip", dados, col = "smoker");
plt.show(sea.lmplot("total_bill", "tip", dados, col = "smoker"))

# Construindo um dataframe com Pandas
df = pd.DataFrame()
# Alimentando o Dataframe com valores aleatórios
df['a'] = random.sample(range(1, 100), 25)
df['b'] = random.sample(range(1, 100), 25)
print(df.head())
# Scatter Plot
#sea.lmplot('a', 'b', data = df, fit_reg = True);
plt.show(sea.lmplot('a', 'b', data = df, fit_reg = True))

# Density Plot
#sea.kdeplot(df.b);
plt.show(sea.kdeplot(df.b))
#sea.kdeplot(df.b, df.a);
plt.show(sea.kdeplot(df.b, df.a))
#sea.distplot(df.a);
plt.show(sea.distplot(df.a))

# Histograma
plt.hist(df.a, alpha = .3)
#sea.rugplot(df.a);
plt.show(sea.rugplot(df.a))
# Box Plot
#sea.boxplot([df.b, df.a]);
plt.show(sea.boxplot([df.b, df.a]))
# Violin Plot
#sea.violinplot([df.a, df.b]);
plt.show(sea.violinplot([df.a, df.b]))
# Heatmap
#sea.heatmap([df.b, df.a], annot = True, fmt = "d");
plt.show(sea.heatmap([df.b, df.a], annot = True, fmt = "d"))
# Clustermap
#sea.clustermap(df);
plt.show(sea.clustermap(df))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
# %matplotlib inline

print("\nTemas")
print("-----")
# Configurações globais para controlar estilo, tamanho de fonte, cores, etc.
sea.set(context="notebook", style="darkgrid", palette="dark")
# Seaborn possui opções de cores variadas
#sea.palplot(sea.color_palette())
plt.show(sea.palplot(sea.color_palette()))
#sea.palplot(sea.color_palette("husl", 8))
plt.show(sea.palplot(sea.color_palette("husl", 8)))
#sea.palplot(sea.color_palette("hls", 8))
plt.show(sea.palplot(sea.color_palette("hls", 8)))

#sea.palplot(sea.color_palette("coolwarm", 7))
plt.show(sea.palplot(sea.color_palette("coolwarm", 7)))

#sea.palplot(sea.cubehelix_palette(8))
plt.show(sea.palplot(sea.cubehelix_palette(8)))

# O método tsplot cria plots a partir de séries temporais
gammas = sea.load_dataset("gammas")
#sea.tsplot(gammas, "timepoint", "subject", "ROI", "BOLD signal", color = "muted");
plt.show(sea.tsplot(gammas, "timepoint", "subject", "ROI", "BOLD signal", color = "muted"))

print("\nOutros Plots")
print("------------")
# Histogramas com subsets dos dados
sea.set(style = "darkgrid")

dados = sea.load_dataset("tips")
g = sea.FacetGrid(dados, row = "sex", col = "time", margin_titles = True)
bins = np.linspace(0, 60, 13)
#g.map(plt.hist, "total_bill", color = "steelblue", bins = bins, lw = 0);
plt.show(g.map(plt.hist, "total_bill", color = "steelblue", bins = bins, lw = 0))

# Diversos plots simultâneos
sea.set(style = "white", palette = "muted")
f, axes = plt.subplots(2, 2, figsize = (7, 7), sharex = True)
sea.despine(left = True)

rs = np.random.RandomState(10)

b, g, r, p = sea.color_palette("muted", 4)

d = rs.normal(size = 100)

sea.distplot(d, kde = False, color = b, ax = axes[0, 0])
sea.distplot(d, hist = False, rug = True, color = r, ax = axes[0, 1])
sea.distplot(d, hist = False, color = g, kde_kws = {"shade": True}, ax = axes[1, 0])
sea.distplot(d, color = p, ax = axes[1, 1])

plt.setp(axes, yticks = [])
plt.tight_layout()

# Plot com distribuições marginais
from scipy.stats import kendalltau
sea.set(style="ticks")

rs = np.random.RandomState(11)
x = rs.gamma(2, size = 1000)
y = -.5 * x + rs.normal(size = 1000)
#sea.jointplot(x, y, kind = "hex", stat_func = kendalltau, color = "#4CB391");
plt.show(sea.jointplot(x, y, kind = "hex", stat_func = kendalltau, color = "#4CB391"))

# Regressão Logística
sea.set(style = "darkgrid")
df = sea.load_dataset("titanic")

pal = dict(male = "#6495ED", female = "#F08080")
g = sea.lmplot("age", "survived", col = "sex", hue = "sex", data = df, palette = pal,
               y_jitter = .02, logistic = True)
g.set(xlim=(0, 80), ylim = (-.05, 1.05));

# Regressão Linear com Distribuições Marginais
sea.set(style = "darkgrid")
tips = sea.load_dataset("tips")
color = sea.color_palette()[2]
g = sea.jointplot("total_bill", "tip", data = tips, kind = "reg", xlim = (0, 60),
                  ylim = (0, 12), color = color, size = 7);

# Pair Plots
sea.set(style = "darkgrid")
df = sea.load_dataset("iris")
#sea.pairplot(df, hue = "species", size = 2.5);
plt.show(sea.pairplot(df, hue = "species", size = 2.5));
