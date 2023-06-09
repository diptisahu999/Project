# django_celery/celery.py

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_employee.settings')

app = Celery('celery_employee')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# app.conf.beat_schedule={
#     'every-10-second':{
#         'task':'api.task.send_email',
#         'schedule':10,
#         'args':('ds8736317@gmail.com',)
#     }
# }


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')