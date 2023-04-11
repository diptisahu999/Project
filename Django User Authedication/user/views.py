from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import LoginForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request,'daseboard.html')
            else:
                return render(request,'user/login.html',{'msg':'Invalid Username and Password'})
    context = {'form': forms}
    return render(request, 'user/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')
