from apscheduler.schedulers.background import BackgroundScheduler
from .models import Data, User

def update_db():
    data = Data.objects.first()
    user = User.objects.all()
    data.big = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data.small = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data.big_maximum = [False, False, False, False, False, False, False, False, False, False, False, False]
    data.small_maximum = [False, False, False, False, False, False, False, False, False, False, False, False]
    data.save()
    for i in user:
        i.button = "a"
        i.save()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_db, 'cron', hour=3, minute=0)
    scheduler.start()