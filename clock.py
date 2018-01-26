from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print(os.environ['STACK_EXCHANGE_ACCESS_TOKEN']
    print(os.environ['STACK_EXCHANGE_KEY'])

sched.start()
