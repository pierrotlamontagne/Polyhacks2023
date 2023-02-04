import numpy as np
import pandas as pd



temp_file = pd.read_csv("../Data/temperature/MTL_A_All_Data.csv")

print(temp_file["Longitude (x)"])