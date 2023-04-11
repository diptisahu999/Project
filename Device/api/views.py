from django.shortcuts import render
from api.serializer import AreaListSerializer,DepartmentListSerializer,SubAreaListSerializer,DeviceListSerializer,STBChannelListSerializer,CroppedAreaListSerializer,IconListSerializer

# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from .models import *

# Area_views here.
class Area_Listviews(generics.ListCreateAPIView):
    queryset=Area.objects.all()
    serializer_class=AreaListSerializer

class Area_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=Area.objects.all()
    serializer_class=AreaListSerializer

# Departments_views here
class Departments_Listviews(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentListSerializer

class Departments_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=Department.objects.all()
    serializer_class=DepartmentListSerializer


# SubArea_views here.

class SubArea_Listviews(generics.ListCreateAPIView):
    queryset=SubArea.objects.all()
    serializer_class=SubAreaListSerializer

class SubArea_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=SubArea.objects.all()
    serializer_class=AreaListSerializer

# Devices_views here
class Devices_Listviews(generics.ListCreateAPIView):
    queryset=Devices.objects.all()
    serializer_class=DeviceListSerializer
    # print(serializer_class)


class Devices_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=Devices.objects.all()
    serializer_class=DeviceListSerializer

# STBChannels_views Here
class STBChannels_Listviews(generics.ListCreateAPIView):
    queryset=STBChannels.objects.all()
    serializer_class=STBChannelListSerializer

class STBChannels_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=STBChannels.objects.all()
    serializer_class=STBChannelListSerializer

# CroppedArea_views here
class CroppedArea_Listviews(generics.ListCreateAPIView):
    queryset=CroppedArea.objects.all()
    serializer_class=CroppedAreaListSerializer
    # print(queryset)

class CroppedArea_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=CroppedArea.objects.all()
    serializer_class=CroppedAreaListSerializer
    # print(queryset)


# Icon_views Here

class Icon_Listviews(generics.ListCreateAPIView):
    queryset=Icon.objects.all()
    serializer_class=IconListSerializer

class Icon_DetailsViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field="pk"
    queryset=Icon.objects.all()
    serializer_class=IconListSerializer



# def Area_view():
#     area = Area.objects.all()
#     data['name'] = i [for i in area]
    
#     print(data)
    
# Area_view()


