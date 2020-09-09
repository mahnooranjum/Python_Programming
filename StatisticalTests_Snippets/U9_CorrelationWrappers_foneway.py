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
from scipy import stats

data = pd.read_csv('data/combined_kmeans25_100.csv')

method = 'f_oneway'
def custom(a, b):
    v,p = stats.f_oneway(a, b)
    return v

corr_mat = data.corr(method = custom)

fig, ax = plt.subplots(1,1, figsize = (10,4))
ax = sns.heatmap(corr_mat, cmap = 'Blues_r', linewidths=.5, annot=True)
ax.set_title(str(method))
plt.savefig(str(method) + '.png')
