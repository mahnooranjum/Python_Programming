'''
    Mahnoor Anjum
    Snippets:
        pykrige
    Reference:
        Official documentation
'''

import numpy as np
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

path = 'data/private.txt'
data = pd.read_csv(path, delimiter='\t')

cols = ['X', 'Y', 'Z']
data = data[cols].values

data = data[1:500, :]

from sklearn.preprocessing import StandardScaler
obj = StandardScaler()
data = obj.fit_transform(data)

gridx = np.linspace(min(data[:,0]), max(data[:,0]), 50)
gridy = np.linspace(min(data[:,0]), max(data[:,0]), 50)


obj = OrdinaryKriging(data[:, 0], data[:, 1], data[:, 2], variogram_model='gaussian',
                     verbose=False, enable_plotting=True)


Z, SS = obj.execute('grid', gridx, gridy)
X,Y = np.meshgrid(gridx,gridy)

# Writes the kriged grid to an ASCII grid file.
# kt.write_asc_grid(gridx, gridy, Z, filename="output.asc")
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=1)
ax.set_title('Meshgrid wireframe')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('M')

