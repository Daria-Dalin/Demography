import json


pets_info = {
    'pets': [
        {
            'pet': 'dog',
            'name': 'Reks',
            'food': 'Purina',
            'age': 4
        },
        {
            'pet': 'cat',
            'name': 'Matilda',
            'food': 'Whiskas',
            'age': 3
        }
    ]
}

#with open('data.pickle', 'wb') as f:
 #   pickle.dump(pets_info, f)

#сериализация json
#with open('pets.json', 'w') as f:
  #  json.dump(pets_info, f)

#десериализация json
with open('pets.json', 'r') as f:
   temp = json.load(f)
print(temp)

#print(pets_info['pets'][0]['name'])