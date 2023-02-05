import numpy as np
import pickle 
from glob import glob

DataDir = './data_birds*'

files_birds = sorted(glob(DataDir))
data_whole = []


for files in files_birds:
    with open(files, 'rb') as f : 
        data_month = pickle.load(f)
    f.close
