#!/usr/local/opt/python/libexec/bin/python

import pandas as pd
import seaborn as sns; sns.set(color_codes=True)

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab
import matplotlib as mpl

# Scientific libraries
import numpy as np
import scipy as sy
from scipy import stats
import plotly
import matplotlib.font_manager

from statsmodels.compat import lzip
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv("data/book-sales.csv")
y = data['Units']
x = data['Year']

# font_manager.findfont('Source Sans Pro')
plt.xlabel('', fontname='Source Sans Pro')
plt.ylabel('Books in thousands', fontname='Source Sans Pro')
plt.plot(x,y)
plt.ylim(400, 1800)
plt.gca().get_yaxis().set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plt.savefig("media/book-sales.eps", format='eps')
plt.savefig("media/book-sales.png", format='png')

data = pd.read_csv("data/market-growth.csv")
y = data['Units']
x = data['Year']

# font_manager.findfont('Source Sans Pro')
plt.xlabel('', fontname='Source Sans Pro')
plt.ylabel('Revenue in billions', fontname='Source Sans Pro')
plt.plot(x,y)
plt.ylim(7, 12)
plt.xlim(2017.5, 2024.5)
formatter = mpl.ticker.FormatStrFormatter('$%1.1f')
plt.gca().get_yaxis().set_major_formatter(formatter)
plt.savefig("media/market-growth.eps", format='eps')
plt.savefig("media/market-growth.png", format='png')
