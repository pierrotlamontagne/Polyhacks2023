import numpy as np
import pickle 
from glob import glob

# DataDir = './data_birds*'

# years = list(range(2019, 2023))
# months = list(range(1, 13))
# data_whole = []

# for year in years : 
#     # print(year)   

#     if year == 2023 :
#         month = 1
       
#         with open('../Data/Birds/data_birds_'+str(year)+'_'+str(month)+'.pickle', 'rb') as f :
#             data_month = pickle.load(f)
#         f.close
#         data_whole.append(data_month)

#     else :
#         for month in months :
#             print(month)
#             print(year)
#             with open('../Data/Birds/data_birds_'+str(year)+'_'+str(month)+'.pickle', 'rb') as f :
#                 data_month = pickle.load(f)
#                 print(data_month)
#             f.close
#             data_whole.append(data_month)

# # # print(data_whole)
# with open('../Data/Birds/data_birds_whole.pickle', 'wb') as f :
#     pickle.dump(data_whole,f)
# f.close()




with open('../Data/Birds/data_birds_whole.pickle', 'rb') as f :
    data_whole = pickle.load(f)
f.close()

HowManyBirds = 0

nameBirds = []

print(data_whole)

for data in data_whole : 

    namebirds = data.iloc[:,0]
    nameBirds.append(namebirds.iloc[0])

EveryBird = []
for birds in nameBirds:
    for bird in birds : 
        EveryBird.append(bird)

Set_Birds = np.array(list(set(EveryBird)))

counts_birds = []
for bird in Set_Birds : 
    counts_birds.append(EveryBird.count(bird))

counts_birds = np.array(counts_birds)
idx_max_sightings = np.where(counts_birds == max(counts_birds))[0]

print(Set_Birds[idx_max_sightings])




# print(len(EveryBird))
    