'''
    Mahnoor Anjum
    Python:
        Bivariate Analysis
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random 

sns.set(color_codes=True)

savepath = 'data/private/saveslice/'
filename = 'v3_1'
genpath = 'data/private/gen/'
genname = 'g3_1'


for i in [500, 1000, 2000, 3000]:
    _temp = pd.read_csv(savepath + filename + '_' + str(i) + '.csv')
    ax = plt.figure()
    sns.jointplot(x="x1", y="x2", data=_temp)
    plt.title(i)
    
