import numpy as np
import requests
import json
from scipy.io import savemat
import pickle

months_day = [(1,31), (2, 28), (3, 31), (4, 30), (5, 31), (6,30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]  

data_birds_all_period = [] 

years = [2023, 2022, 2021, 2020, 2019]

for year in years : 

    print('year :', year)

    if year == 2023 : 

        j = months_day[0]
        month = j[0]
        print(month)
        for day in range(1, j[1]+1) : 
            print('Day : ', day)

            url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/historic/"+str(year)+'/'+str(month)+'/'+str(day)

            payload={}
            headers = {
            'X-eBirdApiToken': 'srd8gruimurh'
            }

            response = requests.get(url_recent, headers=headers, data=payload)

            data_bird = json.loads(response.text)
            name, obsdate, howmany, lat, lon = np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str)
                
            j = 0
            for i in data_bird : 
                # print(data_bird)

                if "howMany" in i.keys() : 
                    howmany[j] = i["howMany"]

                else : 
                    howmany[j] = 1

                name[j] = i["comName"]
                obsdate[j] = i["obsDt"]
                # print(i["howMany"])
                

                lat[j] = i["lat"]
                lon[j] = i["lng"]
                j += 1

            data_birds_day = np.zeros((len(data_bird), 5),  dtype=str)
            data_birds_day[:, 0] = name
            data_birds_day[:, 1] = obsdate
            data_birds_day[:, 2] = howmany
            data_birds_day[:, 3] = lat
            data_birds_day[:, 4] = lon
            data_birds_all_period.append(data_birds_day)
    
    else : 
        for j in months_day : 

            month = j[0]
            print('Month : ', month)

            for day in range(1, j[1]+1) : 

                print('Day : ', day)

                url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/historic/"+str(year)+'/'+str(month)+'/'+str(day)

                payload={}
                headers = {
                'X-eBirdApiToken': 'srd8gruimurh'
                }

                response = requests.get(url_recent, headers=headers, data=payload)

                data_bird = json.loads(response.text)
                name, obsdate, howmany, lat, lon = np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str), np.zeros(len(data_bird),  dtype=str)
                
                j = 0
                for i in data_bird : 
                    # print(data_bird)

                    if "howMany" in i.keys() : 
                        howmany[j] = i["howMany"]

                    else : 
                        howmany[j] = 1

                    name[j] = i["comName"]
                    obsdate[j] = i["obsDt"]
                    # print(i["howMany"])
                    

                    lat[j] = i["lat"]
                    lon[j] = i["lng"]
                    j += 1

                data_birds_day = np.zeros((len(data_bird), 5),  dtype=str)
                data_birds_day[:, 0] = name
                data_birds_day[:, 1] = obsdate
                data_birds_day[:, 2] = howmany
                data_birds_day[:, 3] = lat
                data_birds_day[:, 4] = lon
                data_birds_all_period.append(data_birds_day)


        with open('data_birds_{}.pickle'.format(year), 'wb') as f:
            pickle.dump(data_birds_all_period, f)
        # Data_Birds = {'Data', data_birds_all_period}
        # savemat('Data_Birds.mat', Data_Birds)

        
