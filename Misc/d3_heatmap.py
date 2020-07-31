'''
    Mahnoor Anjum
    Python:
        Trivariate Analysis
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random 
from mpl_toolkits.mplot3d import Axes3D
# sns.set()


path = 'data/private/savepath/'
filename = 'v3_1'
genpath = 'data/private/gen/'
genname = 'g3_1'

data = pd.read_csv(path + filename+'.csv')
gen = pd.read_csv(genpath + genname + '.csv')

k = 50
data = data.sample(k)

x = data['x1']
y = data['x2']
z = data['x3']

fig = plt.figure(figsize=(20,20))

data = pd.DataFrame({'X': x, 'Y': y, 'Z': z})
data_pivoted = data.pivot("X", "Y", "Z")
ax = sns.heatmap(data_pivoted)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title(str(k)+"_samples")

