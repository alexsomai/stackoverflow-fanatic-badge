import os
from datetime import datetime, timedelta
from pprint import pprint

import requests
import logging
from requests_oauthlib import OAuth2Session


def get_authorization_url():
    client_id = os.environ['STACK_EXCHANGE_CLIENT_ID']
    redirect_uri = 'https://stackexchange.com/oauth/login_success'
    scope = 'no_expiry'

    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = oauth.authorization_url('https://stackexchange.com/oauth/dialog')

    logging.basicConfig(level=logging.INFO)
    logging.info("Access the following URL to obtain the access token: %s", authorization_url)
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


def have_logged_in(delta_hours):
    """
    Check whether the user identified by the OS environment variables have logged in on the Stack Overflow site
    for the last delta_hours
    :param delta_hours: <int> the timedelta expressed in hours to verify since the user have logged in
    :return: <bool> True if the user have logged in the last delta_hours, False otherwise
    """
    user_details = get_user_details()
    last_access_date_timestamp = user_details['items'][0]['last_access_date']

    last_access_date = datetime.fromtimestamp(last_access_date_timestamp)

    now = datetime.now()
    return last_access_date > now - timedelta(hours=delta_hours)


if __name__ == "__main__":
    get_user_details()
