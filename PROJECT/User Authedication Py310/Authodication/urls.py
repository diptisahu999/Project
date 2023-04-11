# from django.conf.urls import url 
from django.urls import include, path,re_path
from Authodication import views 
 
urlpatterns = [ 
    path('api/', views.tutorial_list),
    path('api/<int:pk>', views.tutorial_detail),
    path('api/tutorials/', views.tutorial_list_published)
]
