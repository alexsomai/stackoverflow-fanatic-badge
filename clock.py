import logging
import logging.config

from apscheduler.schedulers.blocking import BlockingScheduler

import stack_exchange_api
import stack_overflow_page
from sendgrid_helper import send_mail

logging.config.fileConfig('logging.conf')
schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=3)
def access_stack_overflow_page():
    stack_overflow_page.login()


@schedule.scheduled_job('interval', hours=3)
def access_stack_overflow_api():
    delta_hours = 12

    if stack_exchange_api.have_logged_in(delta_hours) is False:
        message = "You haven't logged in for at least " + str(delta_hours) + " hours! \n " + \
                  "Access stackoverflow.com to save your login streak"
        logging.error(message)
        send_mail("Login overdue alert!", message)


schedule.start()
