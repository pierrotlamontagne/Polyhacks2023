import numpy as np
import requests
import lxml.html as lh
import json



url_recent = "https://ebird.org/region/CA-QC-MR"

page = requests.get(url_recent)

doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
print(tr_elements)


countries = []

for i in range(2, len(tr_elements)):
    T = tr_elements[i]
    
    for t in T.iterchildren():
        data = t.text_content()
        data = unicodedata.normalize('NFKD', data)
        l = len(data)
        # if (j==0):
        #     print(data)
        if j==0:
            cut_p = data.find("\\")
            country.append(data[1:cut_p])
        if j==1:
            country.append(data[:(l-1)])
        if j==3:
            country.append(data[:(l-1)])
        if j==5:
            country.append(data[:(l-1)])
        j+=1
    countries.append(country)
    country = []

output = "{"
for country in countries:
    output+=("{\""+country[0]+"\",\""+country[1]+"\",\""+country[2]+"\","+country[3]+"},")
output+="}"
print(output)


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
    
