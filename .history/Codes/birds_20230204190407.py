import numpy as np
import requests
import json
from scipy.io import savemat
import pickle

months_day = [(1,31), (2, 28), (3, 31), (4, 30), (5, 31), (6,30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]  

data_birds_all_period = [] 

years = [2022, 2021, 2020, 2019]

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
            name, obsdate, howmany, lat, lon = [],[],[],[],[]
            j = 0
            for i in data_bird : 


                if "howMany" in i.keys() : 
                    howmany.append(i["howMany"])

                else : 

                    howmany.append('1')

                name.append(i["comName"])
                obsdate.append(i["obsDt"])
                lat.append(i["lat"])
                lon.append(i["lng"])
                j += 1


            day = {'Name': name, 'obsdate': obsdate, 'how_many' : howmany, 'lat': lat, 'lon': lon}

                

            data_birds_all_period.append([name, obsdate, howmany,lat,lon])

        with open('data_birds_{}.pickle'.format(year), 'wb') as f:
            pickle.dump(data_birds_all_period, f)
        f.close()
    
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
                name, obsdate, howmany, lat, lon = [],[],[],[],[]
                j = 0
                for i in data_bird : 


                    if "howMany" in i.keys() : 
                        howmany.append(i["howMany"])

                    else : 

                        howmany.append('1')

                    name.append(i["comName"])
                    obsdate.append(i["obsDt"])
                    lat.append(i["lat"])
                    lon.append(i["lng"])

                    j += 1

                data_birds_all_period.append([name, obsdate, howmany,lat,lon])
        if (month == 6) or (month == 12) : 
            with open('data_birds_{}_{}.pickle'.format(year,j), 'wb') as f:
                pickle.dump(data_birds_all_period, f)
            f.close()


        
