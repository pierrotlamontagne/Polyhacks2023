import pandas as pd
import numpy as np

data = pd.read_csv("../Data/temperature/temp_data_2021.csv",delimiter=",")

temp = data["Mean Temp (°C)"]