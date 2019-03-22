#!/usr/local/opt/python/libexec/bin/python

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

from statsmodels.compat import lzip
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv("data/econ-wk2-4.csv")
x = data['Units']
y = data['Price']

ax = sns.regplot(x="Units", y="Price", data=data)
ax.set_ylim(0,)
ax.set_xlim(0,)
beef_model = ols("Units ~ Price", data=data).fit()
print(beef_model.summary())

fig = ax.get_figure()
fig.savefig("images/econ/wk2-4.png")
