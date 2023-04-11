from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_delete,post_save

@receiver(user_logged_in,sender=User)
def login_success(sender, request, user,**kwargs):
    print("------------------")
    print("login signal.. intro")
    print("Sender: ",sender)
    print("Request:  ",request)
    print("User:  ",user)
    print("User Password:",user.password)
    print(f'kwarge:{kwargs}')
    # user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out,sender=User)
def logout_success(sender, request, user,**kwargs):
    print("------------------")
    print("logout signal.. intro")
    print("Sender: ",sender)
    print("Request:  ",request)
    print("User:  ",user)
    print("User Password:",user.password)
    print(f'kwarge:{kwargs}')

@receiver(user_login_failed)
def login_failed(sender, request, credentials ,**kwargs):
    print("------------------")
    print("logout signal.. intro")
    print("Sender: ",sender)
    print("Request:  ",request)
    print("Credentials:  ",credentials)
    print(f'kwarge:{kwargs}')


@receiver(pre_save,sender=User)
def ancd(sender,instance,**kwargs):
    print("------------------")
    print("save data.. intro")
    print("Sender: ",sender)
    print("Request:  ",instance)
    print(f'kwarge:{kwargs}')    