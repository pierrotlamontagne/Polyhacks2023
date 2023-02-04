import numpy as np
import pandas as pd



temp_file = pd.read_csv("../Data/temperature/MTL_A_All_Data.csv")

longitude = temp_file["Longitude (x)"][0]
latitude  = temp_file["Latitude (y)"][0]

temp_array =  np.genfromtxt("../Data/temperature/MTL_A_All_Data.csv", delimiter=',')

# index = temp_file[temp_file['Year'] == '2021'].index()[0]

print(temp_array)
