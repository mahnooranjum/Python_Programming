'''
    Mahnoor Anjum
    Python:
        Clusters
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random 

filename = 'private'
path = 'data/' + filename + '.txt'
data = pd.read_csv(path, delimiter='\t')

columns = ['X','Y','Z']
X = data[columns]


data.isnull().sum()

from sklearn.preprocessing import MinMaxScaler
obj = MinMaxScaler()
X_scaled = obj.fit_transform(X)

from sklearn.mixture import GaussianMixture
model = GaussianMixture(n_components = 300)
model.fit(X_scaled)
y_pred = model.predict(X_scaled)

data = X.join(pd.DataFrame({'Cluster':y_pred}))
data.to_csv('data/clusters/' + filename  + '.csv', index=None)
