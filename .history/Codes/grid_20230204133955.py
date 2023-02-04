import numpy as np

""""
Montréal Dimensions : 
    boomerang -> 52 km par 18 km
    rectangle -> 52 km par 18 km  
"""
latlong_longueur1 = [45.417665, -73.96712]
latlong_longueur2 = [45.702069, -73.477873]


x = np.linspace(latlong_longueur1[0], latlong_longueur2[0], 10000)
y = np.arange(0, 18*1000, 25)

X_grid, Y_grid = np.meshgrid(x, y)

