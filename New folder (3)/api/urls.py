from django.urls import path
from .import views

urlpatterns = [
    path('',views.EmailAPI.as_view())
]


#hit this link 
#http://127.0.0.1:8000/?subject=Demo&text=Test&recipient_list=diptiranjansahu999@gmail.com
