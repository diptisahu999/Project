from django.urls import path
from api import views

urlpatterns=[
    path('singer',views.SingerList.as_view()),
    path('singer/<int:pk>',views.SingerDetails.as_view()),


    path('song',views.SongList.as_view()),
    path('song/<int:pk>',views.SongDetails.as_view()),

]