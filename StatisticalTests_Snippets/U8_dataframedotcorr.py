# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:35:45 2020

@author: Mahnoor
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# filename = 'combined_kmeans25_100_CW_1'
# path = 'quickascend/'+filename+'.csv'

path = 'clusters/combined_kmeans25_rssi_100.csv'
data = pd.read_csv(path)



# columns = ['X','Y','Distance (m)','M (dBm)']
# data = data[columns]

fig = plt.figure(figsize=(10,10))

cmap = sns.diverging_palette(220, 10, as_cmap=True)
corr = data.corr()
sns.heatmap(corr,  cmap=cmap, center=0, annot = True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})