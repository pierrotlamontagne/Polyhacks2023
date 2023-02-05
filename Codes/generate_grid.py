import numpy as np
import random as rand
import json

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

mtl_poly = Polygon(
    [
    (45.407230, -73.957201),
    (45.437012, -73.969255),
    (45.510384, -73.849193),
    (45.546528, -73.692003),
    (45.628188, -73.621605),
    (45.680091, -73.531438),
    (45.689186, -73.483702),
    (45.551593, -73.529027),
    (45.470159, -73.551689),
    (45.416031, -73.614855),
    (45.437688, -73.756615),
    (45.419754, -73.876677),
    (45.406891, -73.919109),
    ]
)

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

        point = Point(x[i],y[j])

        if mtl_poly.contains(point):

            feat_dict = {
                "type":"Feature",
                "geometry":{
                    "type":"Polygon",
                    "coordinates":[[[y[j],x[i]],[y[j+1],x[i]],[y[j+1],x[i+1]],[y[j],x[i+1]],[y[j],x[i]]]],
                },
                "properties":{
                    "probPerSector":rand.randint(1,7),
                    "probPerSector2":rand.randint(1,7),
                },
            }

            dict["features"].append(feat_dict)

json_object = json.dumps(dict)

with open("./Data/test_grid.json","w") as outfile:
    outfile.write(json_object)

