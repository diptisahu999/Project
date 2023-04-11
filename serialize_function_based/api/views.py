from django.shortcuts import render
from rest_framework.decorators import api_view 
from .serializers import Serializers
from .models import Student
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST'])
def studentlistview(request):
    if request.method=='GET':
        stu_list=Student.objects.all()
        serializer=Serializers(stu_list,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['DELETE','PUT','GET'])
def studentdetailview(request,pk):
    try:
        student=Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=404)
    if request.method=="DELETE":
        student.delete()
        return Response({'data':'data delete successfully!!!'})
    elif request.method=='GET':
        serializer=Serializers(student)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=Serializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data update successfully!!!','alldata':serializer.data})
    else:
        return Response(serializer.errors)
    

