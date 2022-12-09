import requests, json

def get_pokemon_info(pokemon):
    new_data = []
    
    pokemon_dict = {}
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    pokemon_dict[pokemon] = {
        'name':f'{pokemon}',
        'ability':response.json()["abilities"][0]["ability"]["name"],
        'type':response.json()['types'][0]['type']['name'],
        'weight':response.json()['weight']
        }
    new_data.append(pokemon_dict)
        
    return new_data

response = requests.get('https://pokeapi.co/api/v2/pokemon/')
pokemon_list = []
for x in range(20):
    pokemon_list.append(response.json()['results'][x]['name'])

for pokemon in pokemon_list:
    print(get_pokemon_info(pokemon))