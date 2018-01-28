import os
from pprint import pprint

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

import stack_overflow_page

schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=8)
def access_stack_overflow_page():
    stack_overflow_page.login()


# Temporary remove - the API will be used to verify last_access_date < 24h
# @sched.scheduled_job('interval', minutes=15)
# def access_stackoverflow():
#     site = 'stackoverflow.com'
#     key = os.environ['STACK_EXCHANGE_KEY']
#     access_token = os.environ['STACK_EXCHANGE_ACCESS_TOKEN']
#
#     profile_page_api = 'https://api.stackexchange.com/2.2/me'
#     url = profile_page_api + '?' + 'site=' + site + '&key=' + key + '&access_token=' + access_token
#
#     response = requests.get(url)
#     json = response.json()
#     pprint(json)


schedule.start()
