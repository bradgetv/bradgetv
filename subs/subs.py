# %%
import re
import os
import random
import pandas as pd  
import numpy as np
import plotly.express as px
import plotly.io as pio
# import plotly.graph_objects as go
pio.renderers.default = "browser"

data= pd.DataFrame()
data = pd.read_csv('subs.csv')

fig = px.line(data, x="Datum", y="Aantal subs")

fig.update_layout(
               xaxis_title='Datum',
               yaxis_title="Aantal subs",
               plot_bgcolor='rgba(0,0,0,0)',
               font_family="Arial",
               font_color="black",
               )
a = {'showline' : True,
     'linecolor' : 'black',
     'gridcolor' : 'LightGrey',
     'mirror' : True,
     'zeroline' : True,
     'zerolinecolor' : 'LightGrey',
     'zerolinewidth' : 1}
fig.update_xaxes(a)
fig.update_yaxes(a)
fig.update_yaxes(range=[0, 410])


fig.show()
fig.write_html("subs.html",
                include_plotlyjs='https://cdn.plot.ly/plotly-2.8.3.min.js',
                include_mathjax='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js')