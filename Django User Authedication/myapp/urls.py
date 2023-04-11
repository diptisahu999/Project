from django.urls import path
from .import views
from myapp.views import index, show,delete,edit,daseboard

urlpatterns = [
    path('#',index,name='index'),
    # path('show/',show,name='show'),
     path('daseboard/',daseboard,name='daseboard'),
    path('delete/<int:pk>',delete,name='delete'),
    path('edit/<int:pk>',edit,name='edit'),
   
]
