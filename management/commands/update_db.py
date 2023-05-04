from django.core.management.base import BaseCommand
from datetime import datetime, time, timedelta
from account.models import Data

class Command(BaseCommand):
    help = "Updates database at 3 AM every day"

    def handle(self, *args, **options):
        data = Data.objects.first()
        data.big = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        data.small = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        data.save()