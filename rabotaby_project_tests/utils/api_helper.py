import requests
from rabotaby_project_tests.utils.attach import response_logging, response_attaching


def api_request(base_api_url, endpoint, method, json=None, params=None):
    url = f"{base_api_url}{endpoint}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36'}
    response = requests.request(method, url, json=json, params=params, headers=headers)
    response_logging(response)
    response_attaching(response)
    return response
