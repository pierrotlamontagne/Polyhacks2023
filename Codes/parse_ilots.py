import pandas as pd
import geopandas as gpd

import sys

# Reading the data

#data1 = pd.read_json("./Data/ilots_chaleur/ilots-de-chaleur-2016.json")
print("Hello")
data = gpd.read_file("./Data/ilots_chaleur/ilots-de-chaleur-2016.geojson")

print(data.head())
