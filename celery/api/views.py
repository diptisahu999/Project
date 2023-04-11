from django.shortcuts import render
from django.http import HttpResponse
from .task import sleepy,send_email

def index(request):
    sleepy.delay(7)
    # sleepy(10) #at list 10 second
    return HttpResponse("<h1>Hello,How are you?<h1>")

def email(request):
    send_email.delay()
    # send_email()
    return HttpResponse("<h1>Email has been send???<h1>")
