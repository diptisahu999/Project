from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from UserOpeartion.models import Employee
from rest_framework.views import APIView
from UserOpeartion.serializer import EmployeeSerializer
from rest_framework.response import Response 
from rest_framework import status,serializers
from rest_framework.permissions import IsAuthenticated
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import get_object_or_404

# Create your views here.
def employee_register(request):
    if request.method!='POST':
        return HttpResponse("THIS METHOD IS NOT RIGHT")

    firstName=request.data['fname']
    lastName=request.data['lname']
    age=request.data['age']
    dob=request.data['dob']
    address=request.data['address']
    status=request.data['status']
    gender=request.data['gender']
    # print(firstName,lastName,age,address,status,dob,gender)
    emp_data=Employee(first_name=firstName,last_name=lastName,age=age,dob=dob,address=address,gender=gender,status=status)
    emp_data.save()
    return HttpResponse("Employee Registration successfully")

class EmployeeOpr(APIView):
    def get(self,request):
        employee_data=Employee.objects.all()
        serializer=EmployeeSerializer(employee_data,many=True)
        return Response(serializer.data)
    # return HttpResponse("Get Method")
    def post(self,request):        
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            print("damu")
            serializer.save()
            return Response({"Response":"employee created successfully"},status=status.HTTP_200_OK)
        else:
            print("not valid")
            return HttpResponse({"Response":"invalid data"},status=status.HTTP_404_NOT_FOUND)
# def add_user(request):
#     if request.method!='POST':
#         return HttpResponse("THIS METHOD IS NOT RIGHT")
#     firstName=data['fname']
#     lastName=data['lname']
#     age=data['age']
#     dob=data['dob']
#     address=data['address']
#     status=data['status']
#     gender=data['gender']
#     # print(firstName,lastName,age,address,status,dob,gender)
#     emp_data=Employee(first_name=firstName,last_name=lastName,age=age,dob=dob,address=address,gender=gender,status=status)
#     emp_data.save()

def websocket_update_user(id,data):
    print(data)
    firstName=data['first_name']
    lastName=data['last_name']
    age=data['age']
    dob=data['dob']
    address=data['address']
    status=data['status']
    gender=data['gender']
        # Student_Details_obj=Student_Details.objects.get(id=id)
    Employee_obj=get_object_or_404(Employee,id=id)
    Employee_obj.first_name=firstName
    Employee_obj.last_name=lastName
    Employee_obj.age=age
    Employee_obj.dob=dob
    Employee_obj.address=address
    Employee_obj.gender=status
    Employee_obj.status=gender
    Employee_obj.save()

# def print_update_data(id):
#     employee_data=Employee.objects.get(id=id)
#     return Response(employee_data)
    # serializer=EmployeeSerializer(employee_data,many=True)
    # return Response(serializer.data)
    # return HttpResponse("Get Method")    


# def delete_user(request,id):
#     Employee_obj=Employee.objects.get(id=id)
#     if request.method=='POST':
#         Employee_obj.delete()
def websocket_delete_user(id):
    Employee_obj=Employee.objects.get(id=id)
    Employee_obj.delete()






# def get_user():
#         employee_data=Employee.objects.all()
#         serializer=EmployeeSerializer(employee_data,many=True)
#         return Response(serializer.data)
#     # return HttpResponse("Get Method")    


# {opr_type":"user","opr":"add",{"data":"first_name":"Daminee", "last_name":"Rewatkar","age":21,"dob":"2002-06-04","address":"Vesu Surat  
# Gujrat","gender":"F","status":"A"}}
def websocket_userAdd(data):
    print(data)
    firstName=data['first_name']
    lastName=data['last_name']
    age=data['age']
    dob=data['dob']
    address=data['address']
    status=data['status']
    gender=data['gender']
    # print(firstName,lastName,age,address,status,dob,gender)
    emp_data=Employee(first_name=firstName,last_name=lastName,age=age,dob=dob,address=address,gender=gender,status=status)
    emp_data.save()
    return True

def get_user_list():
    employee_data=Employee.objects.all()
    all_user = []
    for u in employee_data:
        # print(u.first_name)
        obj_user = {
            "id":u.id,
            "first_name":u.first_name,
        "last_name":u.last_name,
        "age":u.age,
        "dob":str(u.dob),
        "address":u.address,
        "gender":u.gender,
        "status":u.status}
        all_user.append(obj_user)
    # print(all_user)
    return all_user
        



    
    