import numpy as np
import requests



url_recent = "https://api.ebird.org/v2/data/obs/{{CA-QC-MR}}"


payload={}
headers = {
  'X-eBirdApiToken': '{{srd8gruimurh}}'
}

response = requests.request("GET", url_recent, headers=headers, data=payload)

print(response.text)