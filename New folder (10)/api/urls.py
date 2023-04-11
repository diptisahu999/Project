from django.urls import path,include
from .import views
from .views import SnippetList,SnippetDetail

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]