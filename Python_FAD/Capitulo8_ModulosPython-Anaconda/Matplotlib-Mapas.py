print("Matplotlib - Mapas")
print("------------------")
print("\nCriando Mapas")
print("-------------")
#Para instalar o basemap, digite no terminal: pip install basemap
# OBS: Se não funcionar, usar o comando: conda install -c anaconda basemap
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
# Mapa do globo terrestre
import warnings
warnings.filterwarnings('ignore')
map = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0)

# Definindo a cor do globo
map.drawmapboundary(fill_color = 'aqua')

# Preenchendo a cor dos continentes
map.fillcontinents(color = 'coral', lake_color = 'aqua')

map.drawcoastlines()

plt.show()
plt.savefig('Globo.png')

# Mapa do globo terrestre expandido
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap()

map.drawcoastlines()

# Mostrar e gravar
plt.show()
plt.savefig('Globo-expandido.png')

# Cria um mapa usando Basemap
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot
from numpy import arange

mapa = Basemap(projection = 'robin', lat_0 = -20, lon_0 = -50,
resolution = 'l', area_thresh = 1e3)

# desenha a costa dos continentes
mapa.drawcoastlines(color='#777799')

# Desenha as fronteiras
mapa.drawcountries(color='#ccccee')

# Pinta os continentes
mapa.fillcontinents(color='#ddddcc')

# Desenha os meridianos
mapa.drawmeridians(arange(0, 360, 30), color='#ccccee')

# Desenha os paralelos
mapa.drawparallels(arange(-180, 180, 30), color='#ccccee')

# Desenha os limites do mapa
mapa.drawmapboundary()

# Mostrar e gravar
plt.show()
pyplot.savefig('Mapa.png', dpi=150)

# Plot contour
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Criando o mapa base
map = Basemap(projection = 'ortho', lat_0 = 45, lon_0 = -100, resolution = 'l')

# Definindo as linhas dos continentes
map.drawcoastlines(linewidth = 0.25)
map.drawcountries(linewidth = 0.25)
map.fillcontinents(color = 'coral', lake_color = 'aqua')

# Desenhando os limites
map.drawmapboundary(fill_color = 'aqua')

# Desenhando latitude e longitude
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))

# Desenhando os grids
nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)

# Projetando coordeandas.
x, y = map(lons*180./np.pi, lats*180./np.pi)

# Dados do mapa
cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
plt.title('Linhas sobre o continente')

# Mostrar e gravar
plt.show()
pyplot.savefig('Continentes.png')

# Mapas dia e noite
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime

# Projeção
map = Basemap(projection='mill',lon_0=180)

# Linhas meridianas e paralelas.
map.drawcoastlines()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])

# Cores
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')

# Sombreando as noites. Time em UTC.
date = datetime.utcnow()
CS=map.nightshade(date)
# plt.title('Mapa Dia/Noite %s (UTC)' % date.strftime("%d %b %Y %H:%M:%S"))
plt.title('Mapa Dia/Noite')

# Mostrar e gravar
plt.show()
pyplot.savefig('Dia-Noite.png')

# Acesse esse site para mais exemplos com Basemap
# http://matplotlib.org/basemap/users/examples.html
