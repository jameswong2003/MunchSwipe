import requests
import urllib

YELP_HOST = 'https://api.yelp.com/v3'
SEARCH_PATH = '/businesses/search'
API_KEY = 'uOLbbY-fBlAGs1rdFA9g-LMxHuQoqrcbnPI1t_tIDvVMCF6WUrsE6TQYAatNCP6M3gB9rNKcB6rAhyIlR09j4MsE42iw7eCAeJdOJde0bEj4yn4tQnfXJv4M6fGkY3Yx'


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
    url = '{0}{1}'.format(host, urllib.quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()

    