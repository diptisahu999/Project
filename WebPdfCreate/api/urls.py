from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.some_view,name='www')
]