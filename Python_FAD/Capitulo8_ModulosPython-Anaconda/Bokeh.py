print("Bokeh")
print("-----")
# Para instalar: pip install bokeh
# Para instalar: pip install bokeh -
# Para instalar: conda install bokeh

# Importando o módulo Bokeh
import bokeh

# Usando output_file para gravar as visualizações
from bokeh.plotting import figure, output_file, show

# Usando output_notebook para visualizar no iPython Notebook
# from bokeh.charts import Bar, output_notebook, show

# Output
# output_notebook()
output_file
# Arquivo gerado pela visualização
output_file("Bokeh-Grafico-Interativo.html")
p = figure()
print(type(p))
print(p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width = 2))
show(p)

# Usando output_notebook para visualizar no iPython Notebook
#from bokeh.charts import Bar, output_notebook, show

# Preparando dados
data = {"y": [1, 2, 3, 4, 5]}
# Output
#output_notebook()
# Criando um novo gráfico
gr = Bar(data, title = "Gráfico Bokeh", xlabel = 'x', ylabel = 'valores', width = 400, height = 400)
# Mostrando os resultados
#show(gr)

# Construindo um ScatterPlot
from bokeh.charts import Scatter, output_file, show

# Preparando os dados
from bokeh.sampledata.autompg import autompg as df

# Criando um Scatter Plot
p = Scatter(df, x = 'mpg', y = 'hp', color = 'cyl',
            title = "Consumo x Potência",
            legend = 'top_right',
            xlabel = "Km/Litro",
            ylabel = "Potência do Motor")

# Especificando o arquivo de saída
output_file("Bokeh-Chart-Interativo.html")

# Visualizando o gráfico
show(p)

# Criando Violin Plots - Seaborn e Bokeh
import seaborn as sea

from bokeh import mpl
from bokeh.plotting import output_file, show

tips = sea.load_dataset("tips")

sea.set_style("whitegrid")

ax = sea.violinplot(x = "day", y = "total_bill", hue = "sex", data = tips,
                    palette = "Set2", split = True,
                    scale = "count", inner = "stick")

output_file("Bokeh-ViolinPlot.html")

show(mpl.to_bokeh())

# Gráficos de Linha
from bokeh.plotting import figure, output_file, show

# Outuput
output_file("Bokeh-Grafico-Linha.html")

p = figure(plot_width = 400, plot_height = 400)

# Adicionando círculos ao gráfico
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size = 20, color = "navy", alpha = 0.5)

# Mostrando o resultado
show(p)

# Geojson
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson

geo_source = GeoJSONDataSource(geojson=geojson)

p = figure()
p.circle(x = 'x', y = 'y', alpha = 0.9, source = geo_source)
output_file("Bokeh-GeoJSON.html")
show(p)

# Plots de Séries Temporais com Pandas
import pandas as pd
from bokeh.plotting import figure, output_file, show

AAPL = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
        parse_dates=['Date']
    )

output_file("Bokeh-Datetime.html")

# create a new plot with a datetime axis type
p = figure(width=800, height=250, x_axis_type="datetime")

p.line(AAPL['Date'], AAPL['Close'], color='navy', alpha=0.5)

show(p)

# Google Maps
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

map_options = GMapOptions(lat=-23.5431786, lng=-46.62918450000001, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="São Paulo"
)

source = ColumnDataSource(
    data=dict(
        lat=[-23.54, -46.62],
        lon=[97.70, 97.74],
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)
