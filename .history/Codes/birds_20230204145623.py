import numpy as np
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import json
import unicodedata



url_recent = "https://ebird.org/region/CA-QC-MR"

page = requests.get(url_recent)

print(page.text)

doc = lh.fromstring(page.content)

print(doc)
tr_elements = doc.xpath('//tr')
# print(tr_elements)

soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 

# countries = []

# for i in range(0, len(tr_elements)):
#     T = tr_elements[i]
    
#     for t in T.iterchildren():
#         data = t.text_content()
#         print(data)



# output = "{"
# for country in countries:
#     output+=("{\""+country[0]+"\",\""+country[1]+"\",\""+country[2]+"\","+country[3]+"},")
# output+="}"
# print(output)


# payload={}
# headers = {
#   'X-eBirdApiToken': 'srd8gruimurh'
# }

# response = requests.get(url_recent, headers=headers, data=payload)

# data_bird = json.loads(response.text)
# print(data_bird)

# Name_birds_species = np.zeros(len(data_bird))
# Observation_data_birds = np.zeros(len(data_bird))



# for i in data_bird :
    
