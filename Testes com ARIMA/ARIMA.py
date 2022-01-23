# %%
import pandas as pd

arquivo = 'dados_new3.csv'
series = pd.read_csv(arquivo, sep=',')

from pandas.plotting import autocorrelation_plot
from matplotlib import pyplot


autocorrelation_plot(series)
pyplot.show()
# %%
