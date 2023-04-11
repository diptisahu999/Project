from django.urls import path
from api import consumers

websocket_urlpatterns=[
    
    path('ws/sc/<str:groupkaname>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),

]