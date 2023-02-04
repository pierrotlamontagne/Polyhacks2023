import pandas as pd
import numpy as np
from grid import x, y

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

for i in range(len(stationId)): 

    #On trouve l'élément de la grid le plus proche de l'emplacement du stationId
    i_Xgrid = find_nearest(latitude[i],x)
    i_Ygrid = find_nearest(longitude[i],y)
    
    air_pollution_dict["x"][i] = i_Xgrid
    air_pollution_dict["y"][i] = i_Ygrid
    
    #On trouve la quantité de polluant
    air_pollution_dict["valeur"][i] = quantite[i]