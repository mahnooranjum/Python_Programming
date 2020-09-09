'''
    Implementation: Mahnoor Anjum 
    Description:
        Intersection Test
    
    By:
        www.geeksforgeeks.org

    
'''

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('data/combined_kmeans25_100.csv')

method = 'pearson'
# method = 'spearman'
# method= 'kendall'
corr_mat = data.corr()


fig, ax = plt.subplots(1,1, figsize = (10,5))
ax = sns.heatmap(corr_mat, cmap = 'YlGnBu', linewidths=.5, annot=True)
ax.set_title(method)
plt.savefig(method + '.png')
