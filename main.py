import requests
import urllib
from urllib.parse import quote

API_HOST = 'https://api.yelp.com/v3'
SEARCH_PATH = '/businesses/search'

API_KEY = 'uOLbbY-fBlAGs1rdFA9g-LMxHuQoqrcbnPI1t_tIDvVMCF6WUrsE6TQYAatNCP6M3gB9rNKcB6rAhyIlR09j4MsE42iw7eCAeJdOJde0bEj4yn4tQnfXJv4M6fGkY3Yx'

SEARCH_LIMIT = 3

def request(host, path, api_key, url_params=None):
    """
    Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()

def search(api_key, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)

print(search(API_KEY, 'Pasta', 'New York'))