import numpy as np
import random as rand
import json

latlong_longueur1 = [45.417665, -73.96712]
latlong_longueur2 = [45.702069, -73.477873]


x = np.linspace(latlong_longueur1[0], latlong_longueur2[0], 500)
y = np.linspace(latlong_longueur1[1], latlong_longueur2[1], 500)

dict = {
    "type": "FeatureCollection",
    "features":[
    ]
}

for i in range(len(x)-1):
    for j in range(len(y)-1):
        feat_dict = {
            "type":"Feature",
            "geometry":{
                "type":"Polygon",
                "coordinates":[[[x[i],y[i]],[x[i],y[i+1]],[x[i+1],y[i+1],x[i+1],y[i]]]],
            },
            "properties":{
                "prob":rand.randint(1,7),
            },
        }

        dict["features"].append(feat_dict)

json_object = json.dumps(dict)

with open("./Data/test_grid.json","w") as outfile:
    outfile.write(json_object)

