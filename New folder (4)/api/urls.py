from django.urls import path
from .import views

urlpatterns = [
    path('',views.ConsultViewSet.as_view())
]
