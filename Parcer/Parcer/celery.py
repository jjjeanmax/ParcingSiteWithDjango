from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Parcer.settings')

app = Celery('Parcer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Обновление данных при необходимости
    'download_and_unzip': {
        'task': 'site_scraping.tasks.download_and_unzip',
        # Каждую 15 секунд
        'schedule': 15,
    },
    # 'get_exchanges_current': {
    #     'task': 'site_scraping.tasks.get_exchanges_current',
    #     # Каждую 15 секунд
    #     'schedule': 20,
    # },
    #
    # 'get_currencies_current': {
    #     'task': 'site_scraping.tasks.get_currencies_current',
    #     # Каждую 20 секунд
    #     'schedule': 20,
    # },
    #
    # 'get_rate_current': {
    #     'task': 'site_scraping.tasks.get_rate_current',
    #     # Каждую 15 секунд
    #     'schedule': 20,
    # },
    #
    #
    # 'get_data': {
    #     'task': 'site_scraping.tasks.get_data',
    #     # Каждую 20 секунд
    #     'schedule': 15,
    # },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
