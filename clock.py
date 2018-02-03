from apscheduler.schedulers.blocking import BlockingScheduler

import stack_overflow_page

schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=1)
def access_stack_overflow_page():
    stack_overflow_page.login()


schedule.start()
