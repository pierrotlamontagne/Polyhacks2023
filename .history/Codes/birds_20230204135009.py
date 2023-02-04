import numpy as np
import requests



url_recent = "https://api.ebird.org/v2/data/obs/{{CA-QC-MR}}/recent"


payload={}
headers = {
  'X-eBirdApiToken': '{{x-srd8gruimurh}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)