from django.urls import path,include
from .import views

urlpatterns = [
    # path('',views.index,name=''),
    path('aa/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# from django.urls import include, path,re_path
# from . import views 
 
# urlpatterns = [ 
#     path('api/', views.tutorial_list),
#     path('api/<int:pk>', views.tutorial_detail),
#     path('api/tutorials/', views.tutorial_list_published)
# ]