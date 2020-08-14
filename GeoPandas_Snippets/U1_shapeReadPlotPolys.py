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


# temp = data['geometry'][idx]
temp = data['geometry'][400:800]
df1 = gpd.GeoDataFrame({'geometry': temp})
temp = data['geometry'][0:400]
df2 = gpd.GeoDataFrame({'geometry': temp})

sets = gpd.overlay(df1, df2, how='union')
ax = sets.plot(alpha=0.5, cmap='tab10')
df1.plot(ax=ax, facecolor='none', edgecolor='k')
df2.plot(ax=ax, facecolor='none', edgecolor='k')

# data.head()
# data.plot()
# plt.show()

