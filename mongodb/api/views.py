from django.shortcuts import render
from rest_framework.decorators import api_view 
from .serializers import Serializers
from .models import Student,Emp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAdminUser



# Create your views here.

# class based views 

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Student.objects.all()
#         serializer = Serializers(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None,):
#         serializer = Serializers(data=request.data)
#         subject= 'Account Registation'
#         massage=f'Hello Your registation Succesfully!!!'
#         # self.task_list = []
#         # taskList = []  
#         # taskViewModel = Serializers["email"]
#         # self.task_list.append(taskViewModel)
#         # # www=[]
#         # ss=request.data.email
#         # www.append(ss)
#         # 'sumankumar26596@gmail.com' 'pratikpatil3095@gmail.com'
#         send_mail(subject,massage,settings.EMAIL_HOST_USER,self.task_list)
#         send_mail(subject,massage,settings.EMAIL_HOST_USER,['sumankumar26596@gmail.com','diptiranjansahu999@gmail.com'])
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class SnippetDetail(APIView):        
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = Serializers(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = Serializers(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  


# generic class based view  

class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Serializers
    

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Serializers
    
    
# Using mixins class based views    
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = Serializers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs) 
    
   
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = Serializers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)   