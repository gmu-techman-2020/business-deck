#!/usr/local/opt/python/libexec/bin/python

# import plotly.plotly as py
# import plotly.graph_objs as go
import pandas as pd
import seaborn as sns; sns.set(color_codes=True)

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
import numpy as np
import scipy as sy
from scipy import stats
import plotly
# plotly.tools.set_credentials_file(username='merovex', api_key='lr1c37zw81')

# xi = np.arange(0,9)
# A = np.array([ xi, np.ones(9)])

# (Almost) linear sequence
# y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
data = pd.read_csv("data/econ-wk2-4.csv")#,names=headers)
x = data['Units Sold']
y = data['Price']

ax = sns.regplot(x="Units Sold", y="Price", data=data)
ax.set_ylim(0,)
ax.set_xlim(0,)
# print(ax)
fig = ax.get_figure()
fig.savefig("images/econ/wk2-4.png")
