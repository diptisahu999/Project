from celery import shared_task
from time import sleep

from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email():
    sleep()
    send_mail("celery task is worked !!!!",
    "do some work!!",
    "ds8736317@gmail.com",
    ["diptiranjansahu999@gmail.com"])
    return None