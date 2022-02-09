import random 
import json

#function that will return a 'meteorite_composition' element
def element_of_meteorite_composition(mete_comp_list):
    i = random.randrange(len(mete_comp_list))
    if(i == 0):
        return mete_comp_list[i]
    elif(i == 1):
        return mete_comp_list[i]
    else:
        return mete_comp_list[i]


#Empty latitude and longitude list 
latitude = []
longitude = []

#meteorite composition list
meterorite_composition = ['stony', 'iron', 'stony-iron']

for i in range(5):
    latitude.append(round(random.uniform(16.0, 18.0), 2))
    longitude.append(round(random.uniform(82.0, 84.0), 2))

# Create a dictionary
meteorite_dictionary = {
    'sites' : [
        {
            'site_id': 1,
            'latitude': latitude[0],
            'longitude': longitude[0],
            'composition': element_of_meteorite_composition(meterorite_composition)
        },
        {
            'site_id': 2,
            'latitude': latitude[1],
            'longitude': longitude[1],
            'composition': element_of_meteorite_composition(meterorite_composition)
        },
        {
            'site_id': 3,
            'latitude': latitude[2],
            'longitude': longitude[2],
            'composition': element_of_meteorite_composition(meterorite_composition)
        },
        {
            'site_id': 4,
            'latitude': latitude[3],
            'longitude': longitude[3],
            'composition': element_of_meteorite_composition(meterorite_composition)
        },
        {
            'site_id': 5,
            'latitude': latitude[4],
            'longitude': longitude[4],
            'composition': element_of_meteorite_composition(meterorite_composition)
        }
    ]
}

#generate a json file
with open('meteorite.json', 'w') as out:
    json.dump(meteorite_dictionary, out, indent = 2)
