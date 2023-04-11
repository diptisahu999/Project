from django.urls import path
from api import views

urlpatterns= [
    #area RestAPI
    path('api/area',views.Area_Listviews.as_view(),name='Area_list_views'),
    path('api/area/<int:pk>',views.Area_DetailsViews.as_view(),name='Area_details_views'),
    #Department RestAPI
    path('api/Department',views.Departments_Listviews.as_view(),name='Department_list_views'),
    path('api/Department/<int:pk>',views.Departments_DetailsViews.as_view(),name='Department_details_views'),
    #Sub Area RestAPI
    path('api/SubArea',views.SubArea_Listviews.as_view(),name='SubArea_list_views'),
    path('api/SubArea/<int:pk>',views.SubArea_DetailsViews.as_view(),name='Subarea_details_views'),
    # Device RestAPI
    path('api/Device',views.Devices_Listviews.as_view(),name='Device_list_views'),
    path('api/Device/<int:pk>',views.Devices_DetailsViews.as_view(),name='Device_details_views'),
    # STB Channels RestAPI
    path('api/STBChannels',views.STBChannels_Listviews.as_view(),name='STBChannels_list_views'),
    path('api/STBChannels/<int:pk>',views.STBChannels_DetailsViews.as_view(),name='STBChannels_details_views'),
    #Cropped Area RestAPI
    path('api/CroppedArea',views.CroppedArea_Listviews.as_view(),name='CroppedArea_list_views'),
    path('api/CroppedArea/<int:pk>',views.CroppedArea_DetailsViews.as_view(),name='CroppedArea_details_views'),
    # Icon RestAPI
    path('api/Icon',views.Icon_Listviews.as_view(),name='Icon_list_views'),
    path('api/Icon/<int:pk>',views.Icon_DetailsViews.as_view(),name='Icon_details_views')
]


# areas>department>subareas>Devices>STB Channel>Croparea>Icon