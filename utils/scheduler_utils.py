from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def scheduler_start():
    scheduler.start()
