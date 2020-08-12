'''
    Implementation: Mahnoor Anjum 
    Description:
        Intersection Test
    
    By:
        www.geeksforgeeks.org

    
'''

import descartes 
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, LineString



data = gpd.read_file('data\shape\shape.shp')

filename = 'collect'
path = 'data/ref/' + filename + '.csv'
lines = pd.read_csv(path)

geodf = gpd.GeoDataFrame({'geometry':data.geometry})
polys = data.geometry
x = lines.X
y = lines.Y

ref = pd.read_csv('data/reference.csv')
xr = ref.loc[0, 'Longitude']
yr = ref.loc[0, 'Latitude']

# for i in range(lines.shape[0]):
#     print(LineString([(xr, yr), (x[i], y[i])]))

idx = np.random.randint(0,lines.shape[0])
line = LineString([(xr, yr), (x[idx], y[idx])])


# poly_gdf = gpd.GeoDataFrame(geometry=[polys])
line_gdf = gpd.GeoDataFrame(geometry=[line]).set_crs("EPSG:4326")

inters = data.geometry.intersects(line)
data[inters].plot()

total = inters.sum()

