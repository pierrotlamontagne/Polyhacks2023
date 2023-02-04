import numpy as np
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import json
import unicodedata



url_recent = "https://ebird.org/region/CA-QC-MR"

page = requests.get(url_recent)
# doc = lh.fromstring(page.content)

# tr_elements = doc.xpath('//tr')


soup = BeautifulSoup(page.content, 'html5lib')
print(soup)
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':"NOM DE L'ESPÈCE"}) 
print(table)
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
    
