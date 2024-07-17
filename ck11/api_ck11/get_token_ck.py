import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_token_ck11():
    api_path = os.getenv('API_PATH')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    try:
        api_address = requests.get(api_path, verify=False)
        api_address_json = json.loads(api_address.content)
        token = requests.post(api_address_json['auth']['tokenEndpointBasic'], auth=(login, password), verify=False)
        token_json = json.loads(token.content)
        token_bearer = 'Bearer ' + token_json['access_token']
        headers = {'Host': token_json['user_host'], 'Authorization': token_bearer, 'Content-Type': "application/json"}

        return headers

    except requests.exceptions.RequestException as e:
        print('Error: ', e)
