# request_with_basic_auth.py

import requests
from requests.auth import HTTPBasicAuth

def send_request():
    # Dummy endpoint
    URL = 'https://api.dummyendpoint.com/data'

    # Dummy credentials for Basic Authentication
    USERNAME = 'dummyUsername'
    PASSWORD = 'dummyPassword'

    response = requests.get(URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    # Print the response
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    send_request()
