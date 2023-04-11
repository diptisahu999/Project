from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Electric_Product,Home_Kitchen_Product,Role
from .serializer import Serializers


class SnippetList(generics.ListCreateAPIView):
    queryset = Electric_Product.objects.all()
    serializer_class = Serializers


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electric_Product.objects.all()
    serializer_class = Serializers
