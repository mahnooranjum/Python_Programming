"""
Created on Fri Aug  7 22:06:33 2020

@author: Mahnoor
"""


import descartes 
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = gpd.read_file('data\shape\shape.shp')

idx = np.random.randint(0,data.shape[0])
# temp = data['geometry'][idx]
temp = data.loc[idx, ['geometry']]
df = gpd.GeoDataFrame({'geometry': temp})
ax = df.plot(color = 'red')

# data.head()
# data.plot()
# plt.show()

