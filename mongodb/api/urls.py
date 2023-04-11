from django.urls import path
from .import views
from .views import SnippetList,SnippetDetail
from .serializers import Serializers
from .models import Student


urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    
]
