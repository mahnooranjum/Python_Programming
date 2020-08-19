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

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 100):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 100), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
plt.clf()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 12, init = 'k-means++')
y_pred = kmeans.fit_predict(X_scaled)
data = X.join(pd.DataFrame({'Cluster':y_pred}))
data.to_csv('data/clusters/' + filename  + '.csv', index=None)
# clusters = np.unique(y_pred)han
# for cluster in clusters:
#     row_idx = np.where(y_pred == cluster)
#     X.loc[row_idx].to_csv('clusters/' + str(cluster) + '_' + filename + '.csv', index=None)
#     plt.scatter(X.loc[row_idx]['X'],X.loc[row_idx]['Y'])

# plt.show()
