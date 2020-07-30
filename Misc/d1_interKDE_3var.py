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
sns.set()

path = 'data/private/savepath360/'
filename = 'f_9'
genpath = 'data/private/gen360/'
genname = 'f_50_2_5000'
# i = 4718sav
data = pd.read_csv(path + filename+'.csv')
gen = pd.read_csv(genpath + genname + '.csv')

gen = gen.iloc[:,[0,1,2]]


gen.dropna(axis=0, inplace=True)
fig, ax = plt.subplots(1,3, figsize=(20,10))
sns.kdeplot(gen["x1"],gen["x2"], ax=ax[0], color='red', label = genname, shade=True)
sns.kdeplot(data["x1"],data["x2"], ax=ax[0], color='blue', label = filename)
ax[0].legend()
ax[0].set_title('x1 v x2')
sns.kdeplot(gen["x2"],gen["x3"], ax=ax[1], color='red', label = genname, shade=True)
sns.kdeplot(data["x2"],data["x3"], ax=ax[1], color='blue', label = filename)
ax[1].legend()
ax[1].set_title('x2 v x3')
sns.kdeplot(gen["x3"], gen["x1"],ax=ax[2], color='red', label = genname, shade=True)
sns.kdeplot(data["x3"], data["x1"],ax=ax[2], color='blue', label = filename)
ax[2].legend()
ax[2].set_title('x3 v x1')
