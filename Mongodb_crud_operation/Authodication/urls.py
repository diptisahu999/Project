# from django.conf.urls import url 
from django.urls import include, path,re_path
from Authodication import views 
 
urlpatterns = [ 
    path('user_api/', views.user_list),
    path('user_api/<int:pk>', views.user),
    path('user_api/uses/', views.user_list_published),
    
    path('role_api/', views.role_list),
    path('role_api/<int:pk>', views.role_detail),
    path('role_api/roles/', views.role_list_published),
    
    path('user_details_api/', views.user_details_list),
    path('user_details_api/<int:pk>', views.user_detail),
    path('role_details_api/users_datails/', views.user_details_list_published),
]
