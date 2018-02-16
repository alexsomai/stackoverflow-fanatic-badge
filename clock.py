from apscheduler.schedulers.blocking import BlockingScheduler

import sendgrid_helper
import stack_exchange_api
import stack_overflow_page

schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=1)
def access_stack_overflow_page():
    stack_overflow_page.login()


@schedule.scheduled_job('interval', hours=1)
def access_stack_overflow_api():
    delta_hours = 12
    if stack_exchange_api.have_logged_in(12) is False:
        message = "You haven't logged in for at least " + str(delta_hours) + " hours! \n " + \
                  "Access stackoverflow.com to save your login streak"
        print("ERROR!\n" + message)
        sendgrid_helper.send_mail("Login overdue alert!", message)


schedule.start()
