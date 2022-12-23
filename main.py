import csv_writer
import requests

YELP_HOST = 'https://api.yelp.com/v3'
API_KEY = 'uOLbbY-fBlAGs1rdFA9g-LMxHuQoqrcbnPI1t_tIDvVMCF6WUrsE6TQYAatNCP6M3gB9rNKcB6rAhyIlR09j4MsE42iw7eCAeJdOJde0bEj4yn4tQnfXJv4M6fGkY3Yx'

response = requests.get(YELP_HOST)
data = ['McDonalds', '$', '4/5', 'my house']
write_data = csv_writer.CSV_Retrieve('database/data.csv')
write_data.add_restaurant(data)