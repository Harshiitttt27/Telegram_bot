import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_bot.settings')

app = Celery('telegram_bot')

# This loads CELERY_ prefixed settings from settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks from all registered Django apps
app.autodiscover_tasks()
