import numpy as np

""""
Montréal Dimensions : 
    boomerang -> 52 km par 18 km
    rectangle -> 52 km par 18 km  
"""

x = np.arange(0, 52*1000, 25)
y = np.arange(0, 18*1000, 25)

X_grid, Y_grid = np.meshgrid(x, y)