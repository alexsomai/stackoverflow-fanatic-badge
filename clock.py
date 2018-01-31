from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler

import sendgrid_helper
import stack_exchange_api
import stack_overflow_page

schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=1)
def access_stack_overflow_page():
    stack_overflow_page.login()


@schedule.scheduled_job('interval', hours=6)
def access_stack_overflow_api():
    user_details = stack_exchange_api.get_user_details()
    last_access_date_timestamp = user_details['items'][0]['last_access_date']

    last_access_date = datetime.fromtimestamp(last_access_date_timestamp)

    now = datetime.now()
    delta_hours = 12
    if last_access_date < now - timedelta(minutes=delta_hours):
        message = "You haven't logged in for at least " + str(delta_hours) + " hours! \n " + \
                  "Access stackoverflow.com to save your login streak"
        print("ERROR!\n" + message)
        sendgrid_helper.send_mail("Login overdue alert!", message)


schedule.start()
