import requests
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from pprint import pprint

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=15)
def access_stackoverflow():
    site = 'stackoverflow.com'
    key = os.environ['STACK_EXCHANGE_KEY']
    access_token = os.environ['STACK_EXCHANGE_ACCESS_TOKEN']

    profile_page_api = 'https://api.stackexchange.com/2.2/me'
    url = profile_page_api + '?' + 'site=' + site + '&key=' + key + '&access_token=' + access_token

    response = requests.get(url)
    json = response.json()
    pprint(json)

sched.start()
