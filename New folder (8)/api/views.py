from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def index(request):
    stu=Student.objects.order_by('-mobile')
    return HttpResponse(stu)
