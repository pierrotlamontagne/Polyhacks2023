import numpy as np
import pickle 
from glob import glob

# DataDir = './data_birds*'

# years = list(range(2019, 2024))
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
print(len(data_whole))
nameBirds = []
i=0
for data in data_whole[-2] : 
    # print(i)
    namebirds = data.iloc[:,0]
    # print(namebirds)
    i+=1
    nameBirds.append(data_whole[i]['Name'])

# print(nameBirds)
    