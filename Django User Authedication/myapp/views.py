from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
        )
        return redirect('show')
    

def show(request):
    dddd=Student.objects.all()
    free={
        'dddd': dddd
    }
    return render(request,'daseboard.html',free)


def delete(request,pk):
    # Student.objects.filter(id=pk).delete()
    Student.objects.get(id=pk).delete()
    return redirect('show')


def edit(request,pk):
    ss=Student.objects.get(id=pk)
    if request.method=='POST':
        ss.name=request.POST['name']
        ss.email=request.POST['email']
        ss.password=request.POST['password']
        ss.mobile=request.POST['mobile']

        ss.save()
        return redirect('show')
    
    return render(request,'edit.html',{'pob':ss})


def daseboard(request):
    dddd=Student.objects.all()
    paginator=Paginator(dddd,1)
    page=request.GET.get('page')
    try:
        dddd=paginator.page(page)
    except EmptyPage:
        dddd=page(paginator.num_pages)
    except PageNotAnInteger:
        dddd=paginator.page(1)
    free={
        'dddd': dddd
    }
    return render(request,'daseboard.html',free)