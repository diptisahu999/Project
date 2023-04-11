from django.urls import path,include
from .import views

urlpatterns = [
    path('as',views.index,name='index'),
]