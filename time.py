import os
import time
from django.core.management import call_command

while True:
    now = time.localtime()
    if now.tm_hour == 3 and now.tm_min == 0 and now.tm_sec == 0:
        call_command("update_db")
    time.sleep(1)