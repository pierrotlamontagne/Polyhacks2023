import pandas as pd
import numpy as np
from grid import x, y
import matplotlib.pyplot as plt

def find_nearest(array, value):
    
    """
    Trouve l'indice du point le plus près d'une valeur donnée dans un array donné

    ### Paramètres
    array: Le array dans lequel chercher l'indice
    value: La valeur pour laquelle on veut trouver le point le plus proche
    
    ### Retourne
    idx: L'indice du point le plus près de la valeur donnée
    
    """
    
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    
    return idx


# Reading the data

data = pd.read_csv("../Data/air_pollution/rsqa-indice-qualite-air-station.csv",delimiter=",")

stationId = data["stationId"]
longitude = data["longitude"]
latitude = data["latitude"]
polluant = data["polluant"]
quantite = data["valeur"] #De 0 à 500

air_pollution_dict = dict()
air_pollution_dict["x"] = np.zeros(len(stationId))
air_pollution_dict["y"] = np.zeros(len(stationId))
air_pollution_dict["valeur"] = np.zeros(len(stationId))

grid_x, grid_y = np.mgrid[0:len(x):500j, 0:len(y):500j]
grid = np.zeros((len(x),len(y)))

for i in range(len(stationId)): 

    #On trouve l'élément de la grid le plus proche de l'emplacement du stationId
    i_Xgrid = find_nearest(latitude[i],x)
    i_Ygrid = find_nearest(longitude[i],y)
    
    #On trouve la quantité de polluant
    valeur = quantite[i]
    air_pollution_dict["valeur"][i] = valeur
    
    sigma_x, sigma_y = 10, 10
    A = valeur
    grid += A * np.exp(-(((grid_x - i_Xgrid)**2 / (2 * sigma_x**2)) + ((grid_y - i_Ygrid)**2 / (2 * sigma_y**2))))
    
air_pollution_dict["grid"] = grid
