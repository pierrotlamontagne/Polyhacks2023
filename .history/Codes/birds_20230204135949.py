# import numpy as np
# import requests
# import json



# url_recent = "https://api.ebird.org/v2/data/obs/CA-QC-MR/recent"
# # https://api.ebird.org/v2/data/obs/{{CA-QC-MR}}/recent


# payload={}
# headers = {
#   'X-eBirdApiToken': '{{srd8gruimurh}}'
# }

# response = requests.get(url_recent, headers=headers, data=payload)

# print(json.loads(response.text))

import requests

url = "https://api.ebird.org/v2/data/obs/KZ/recent"

payload={}
headers = {
  'X-eBirdApiToken': '{{x-ebirdapitoken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)