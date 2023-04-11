from django.urls import path
from api import views

urlpatterns=[
    path('<str:group_name>/',views.index),
]