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

path = 'data/private/savepath/'
filename = 'v3_1'
savepath = 'data/private/saveslice/'
data = pd.read_csv(path + filename+'.csv')

for i in [500, 1000, 2000, 3000, len(data.index)]:
    _temp = data.sample(n=i)
    _temp.to_csv(savepath + filename + '_' + str(i) + '.csv', index=None)
    