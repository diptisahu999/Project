from django.urls import path
from .import views


urlpatterns = [
    path('api',views.studentlistview),
    path('update/<int:pk>',views.studentdetailview)

]
