import numpy as np
import requests
import json



url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/recent"

payload={}
headers = {
  'X-eBirdApiToken': 'srd8gruimurh'
}

response = requests.get(url_recent, headers=headers, data=payload)

data_bird = json.loads(response.text)

for i in data_bird :
    print(i['comName'])
