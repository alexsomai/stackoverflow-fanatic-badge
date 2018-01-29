import os
from pprint import pprint

import requests
from requests_oauthlib import OAuth2Session


def get_authorization_url():
    client_id = '11693'
    redirect_uri = 'https://stackexchange.com/oauth/login_success'
    scope = 'no_expiry'

    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = oauth.authorization_url('https://stackexchange.com/oauth/dialog')

    print("Authorization URL is:", authorization_url)
    return authorization_url


def get_user_details():
    site = 'stackoverflow.com'
    key = os.environ['STACK_EXCHANGE_KEY']
    access_token = os.environ['STACK_EXCHANGE_ACCESS_TOKEN']

    profile_page_api = 'https://api.stackexchange.com/2.2/me'
    url = profile_page_api + '?' + 'site=' + site + '&key=' + key + '&access_token=' + access_token

    response = requests.get(url)
    json = response.json()
    pprint(json)

    return json


get_user_details()
