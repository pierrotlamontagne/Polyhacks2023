import numpy as np
import pickle 
from glob import glob

DataDir = './data_birds*'

files_birds = sorted(glob(DataDir))
data_whole = []

print(files_birds)

years = list(range(2019, 2024))
months = list(range(1, 13))
for year in years : 
    print(year)
    for month in months :
        print(month)
        with open('./data_birds_'+str(year)+'_'+str(month)+'.pickle') as f :
            data_month = pickle.load(f)
        f.close

        data_whole.append(data_month)


