import numpy as np
import pandas as pd

"""
5-> Date/Time,6-> Year, 7-> Month, 8-> Day, 14->Mean Temp (°C), 24-> Total Precip (mm)
"""

date, year, month, Day, Mean_Temp, Total_Precip = 5, 6, 7, 8, 14, 24
# indices_data = [5, 6, 7, 8, 14, 24]

temp_array =  np.genfromtxt("../Data/temperature/MTL_A_All_Data.csv", delimiter=',')


data_date_temp_precip = temp_array[:, [date, year, month, Day, Mean_Temp, Total_Precip]]

