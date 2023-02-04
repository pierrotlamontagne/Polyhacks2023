import numpy as np
import requests
import json



url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/"

payload={}
headers = {
  'X-eBirdApiToken': 'srd8gruimurh'
}

response = requests.get(url_recent, headers=headers, data=payload)

data_bird = json.loads(response.text)
print(data_bird)

Name_birds_species = np.zeros(len(data_bird))
Observation_data_birds = np.zeros(len(data_bird))



for i in data_bird :
    
