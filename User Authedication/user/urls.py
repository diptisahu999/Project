from django.urls import path

from user.views import login_page, logout_page

urlpatterns = [
    path('login/',login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('',login_page, name='login'),
    
]