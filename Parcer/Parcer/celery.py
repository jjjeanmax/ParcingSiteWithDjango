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
    # 'read_status': {
    #     'task': 'site_scraping.tasks.read_status',
    #     # Каждую 15 секунд
    #     'schedule': 15,
    # },
    #
    'save_function': {
        'task': 'site_scraping.tasks.save_function',
        # Каждую 20 секунд
        'schedule': 20,
    },

}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
