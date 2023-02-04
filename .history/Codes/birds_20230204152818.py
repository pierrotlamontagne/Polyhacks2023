import numpy as np
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import json
import unicodedata



# url_recent = "https://api.ebird.org/v2/product/spplist/CA-QC-MR"
url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/historic/2022/1/1"


payload={}
headers = {
  'X-eBirdApiToken': 'srd8gruimurh'
}

response = requests.get(url_recent, headers=headers, data=payload)

data_bird = json.loads(response.text)
print(len(data_bird))

Name_birds_species = np.zeros(len(data_bird))
Observation_data_birds = np.zeros(len(data_bird))



# for i in data_bird :
    
