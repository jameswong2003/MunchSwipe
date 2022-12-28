from yelp_api import Yelp
import json
import random


API_KEY = 'uOLbbY-fBlAGs1rdFA9g-LMxHuQoqrcbnPI1t_tIDvVMCF6WUrsE6TQYAatNCP6M3gB9rNKcB6rAhyIlR09j4MsE42iw7eCAeJdOJde0bEj4yn4tQnfXJv4M6fGkY3Yx'

obj_dump = Yelp.search(api_key=API_KEY, term='Pasta', location='New York')

with open('database/data.json', 'w') as outfile:
    json.dump(obj_dump, outfile, indent=4)

# Choose a random restaurant from the data.json file
infile = open('database/data.json')
data = json.load(infile)
selected_restaurant = random.choice(data['businesses'])
print(json.dumps(selected_restaurant, indent=4))