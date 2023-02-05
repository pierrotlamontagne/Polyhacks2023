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
        self.pollution_air = air_pollution_dict["grid"][self.x][self.y]
            
        
        



        
    
        