import numpy as np
import pandas as pd
from reading_air_pollution import air_pollution_dict
from reading_meteo import temp, precipitation

class point: 
    def __init__(self,x,y,t):
        
        #Coordonnées de la cas
        self.x = x 
        self.y = y
        
        #Temps
        self.t = t #From 0 to 364
        
        #fill météo
        self.temperature = temp[t]
        self.precipitation = precipitation[t]
    
        #fill pollution air
        i_station = np.where((air_pollution_dict['x'] == self.x) & (air_pollution_dict['y'] == self.y))
        print(i_station)
        if len(i_station[0])==0: 
            self.pollution_air = 0
            
        else: 
            self.pollution_air = air_pollution_dict["valeur"][i_station]
            
        
        



        
    
        