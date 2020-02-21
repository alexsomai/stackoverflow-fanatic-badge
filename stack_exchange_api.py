import logging
import logging.config
import os
from datetime import datetime, timedelta
from pprint import pformat

import requests
from requests_oauthlib import OAuth2Session

logging.config.fileConfig('logging.conf')


def get_authorization_url():
    client_id = os.environ.get('STACK_EXCHANGE_CLIENT_ID')
    if client_id is None:
        logging.warning("Set 'STACK_EXCHANGE_CLIENT_ID' env variable to obtain the authorization URL")
        return None

    oauth = OAuth2Session(client_id, redirect_uri='https://stackexchange.com/oauth/login_success', scope='no_expiry')
    authorization_url, state = oauth.authorization_url('https://stackexchange.com/oauth/dialog')

    logging.info("Access the following URL to obtain the access token: %s", authorization_url)

    return authorization_url


def get_user_details():
    key = os.environ.get('STACK_EXCHANGE_KEY')
    access_token = os.environ.get('STACK_EXCHANGE_ACCESS_TOKEN')
    if None in (key, access_token):
        logging.warning("Set 'STACK_EXCHANGE_KEY' and 'STACK_EXCHANGE_ACCESS_TOKEN' env variables to retrieve user "
                        "details")
        return None

    profile_page_api = 'https://api.stackexchange.com/2.2/me'
    site = 'stackoverflow.com'

    response = requests.get(profile_page_api, params={'site': site, 'key': key, 'access_token': access_token})
    json_response = response.json()

    logging.debug(pformat(json_response))

    return json_response


def have_logged_in(delta_hours):
    """
    Check whether the user identified by the OS environment variables have logged in on the Stack Overflow site
    for the last delta_hours
    :param delta_hours: <int> the timedelta expressed in hours to verify since the user have logged in
    :return: <bool> True if the user have logged in the last delta_hours, False otherwise
    """
    user_details = get_user_details()
    if user_details is None:
        return None

    last_access_date_timestamp = user_details['items'][0]['last_access_date']
    last_access_date = datetime.fromtimestamp(last_access_date_timestamp)
    now = datetime.now()

    return last_access_date > now - timedelta(hours=delta_hours)


if __name__ == "__main__":
    get_authorization_url()
