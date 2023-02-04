import numpy as np
import requests
import lxml.html as lh
import json



url_recent = "https://ebird.org/region/CA-QC-MR"

page = requests.get(url_recent)

doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
print(tr_elements)




payload={}
headers = {
  'X-eBirdApiToken': 'srd8gruimurh'
}

response = requests.get(url_recent, headers=headers, data=payload)

data_bird = json.loads(response.text)
print(data_bird)

# Name_birds_species = np.zeros(len(data_bird))
# Observation_data_birds = np.zeros(len(data_bird))



# for i in data_bird :
    
