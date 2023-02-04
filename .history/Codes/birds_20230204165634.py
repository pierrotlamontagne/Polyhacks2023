import numpy as np
import requests
import json


months_day = [(1,31), (2, 28), (3, 31), (4, 30), (5, 31), (6,30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]  

data_birds_all_period = [] 

for year in range(2019, 2024) : 

    if year == 2023 : 

        j = months_day[0]
        month = j[0]

        for day in range(1, j[1]+1) : 

            url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/historic/"+str(year)+'/'+str(month)+'/'+str(day)

            payload={}
            headers = {
            'X-eBirdApiToken': 'srd8gruimurh'
            }

            response = requests.get(url_recent, headers=headers, data=payload)

            data_bird = json.loads(response.text)
            name, obsdate, howmany, lat, lon = np.zeros(len(data_bird)), np.zeros(len(data_bird)), np.zeros(len(data_bird)), np.zeros(len(data_bird)), np.zeros(len(data_bird))
                
            j = 0
            for i in data_bird : 

                name[j] = i["comName"]
                obsdate[j] = i["obsDt"]
                howmany[j] = i["howMany"]
                lat[j] = i["lat"]
                lon[j] = i["lon"]
                j += 1

            data_birds_day = np.zeros((len(data_bird), 5))
            data_birds_day[:, 0] = name
            data_birds_day[:, 1] = obsdate
            data_birds_day[:, 2] = howmany
            data_birds_day[:, 3] = lat
            data_birds_day[:, 4] = lon
            data_birds_all_period.append(data_birds_day)

    
    else : 
        for j in months_day : 

            month = j[0]

            for day in range(1, j[1]+1) : 

                url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/historic/"+str(year)+'/'+str(month)+'/'+str(day)

                payload={}
                headers = {
                'X-eBirdApiToken': 'srd8gruimurh'
                }

                response = requests.get(url_recent, headers=headers, data=payload)

                data_bird = json.loads(response.text)
                name, obsdate, howmany, lat, lon = np.zeros(len(data_bird)), np.zeros(len(data_bird)), np.zeros(len(data_bird)), np.zeros(len(data_bird)), np.zeros(len(data_bird))
                
                j = 0
                for i in data_bird : 

                    name[j] = i["comName"]
                    obsdate[j] = i["obsDt"]
                    howmany[j] = i["howMany"]
                    lat[j] = i["lat"]
                    lon[j] = i["lon"]
                    j += 1

                data_birds_day = np.zeros((len(data_bird), 5))
                data_birds_day[:, 0] = name
                data_birds_day[:, 1] = obsdate
                data_birds_day[:, 2] = howmany
                data_birds_day[:, 3] = lat
                data_birds_day[:, 4] = lon
                data_birds_all_period.append(data_birds_day)



    # for i in data_bird :
        
