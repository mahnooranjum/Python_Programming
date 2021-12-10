# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:40:41 2020

@author: Mahnoor
"""


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


sns.set()

data = pd.read_csv('data/combined_kmeans25.csv')

cmap = sns.color_palette("RdBu",n_colors=25)

fig, ax = plt.subplots(1,1,figsize=(10, 8))
sns.swarmplot(x="Cluster", y="M (dBm)", data=data, ax=ax)
plt.savefig('clustered.png')