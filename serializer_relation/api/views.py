from django.shortcuts import render
from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from rest_framework import generics


# Create your views here.
#SINGER CRUD
class SingerList(generics.ListCreateAPIView):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer


class SingerDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer


#SONG CRUD
class SongList(generics.ListCreateAPIView):
    queryset=Song.objects.all()
    serializer_class=SongSerializer


class SongDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    queryset=Song.objects.all()
    serializer_class=SongSerializer







