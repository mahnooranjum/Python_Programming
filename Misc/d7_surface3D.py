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

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)



fig = plt.figure(figsize=(10,7))
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 100, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

