import numpy as np
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import json
import unicodedata
from ebird.api import get_observations

records = get_observations('srd8gruimurh', 'CA-QC-MR')

months_day = [(1,31), (2, 28), (3, 31), (4, 30), (5, 31), (6,30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]  

for i in months_day : 


    url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/historic/2022/"+str(i)+"/*"


    payload={}
    headers = {
    'X-eBirdApiToken': 'srd8gruimurh'
    }

    response = requests.get(url_recent, headers=headers, data=payload)

    data_bird = json.loads(response.text)
    print(data_bird)

    Name_birds_species = np.zeros(len(data_bird))
    Observation_data_birds = np.zeros(len(data_bird))



# for i in data_bird :
    
