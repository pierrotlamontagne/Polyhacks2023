import pickle

f = open("./Codes/data_birds_2023_1.pickle",'rb')
birds = pickle.load(f)
f.close()

print(birds)