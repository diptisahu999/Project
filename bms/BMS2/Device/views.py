from django.shortcuts import render
from Device.models import Bms_bulding_master,Bms_floor_master,Bms_department_master,Bms_sub_area_master,Bms_locker,Bms_device_information
from Device.serializers import Bms_Bulding_master_Serializer,Bms_floor_master_Serializer,Bms_department_master_Serializer,Bms_sub_area_master_Serializer,Bms_locker_Serializer,Bms_Devices_Serializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.

# Bms Bulding Crud Api

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        bms_bulding = Bms_bulding_master.objects.all()    
        bms_bulding_serializer = Bms_Bulding_master_Serializer(bms_bulding, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Bulding Lists", "response":bms_bulding_serializer.data})
        
        
    elif request.method == 'POST':
        bulding_serializers = Bms_Bulding_master_Serializer(data=request.data)
        if bulding_serializers.is_valid():
            bulding_serializers.save()
            # return Response(bulding_serializers.data, status=status.HTTP_201_CREATED) 
            return Response({"data":"true","status_code": "200", "message": "Bulding added Successfully", "response":bulding_serializers.data})
        return JsonResponse(bulding_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_bulding_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    


@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    try: 
        bms_bulding = Bms_bulding_master.objects.get(pk=pk) 
    except Bms_bulding_master.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bms_bulding_serializer = Bms_Bulding_master_Serializer(bms_bulding) 
        # return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":bms_bulding_serializer.data}) 
        return Response(bms_bulding_serializer.data) 
        
    elif request.method == 'PUT': 
        # tutorial_data = JSONParser().parse(request) 
        bms_bulding_serializer = Bms_Bulding_master_Serializer(bms_bulding,data=request.data) 
        if bms_bulding_serializer.is_valid(): 
            bms_bulding_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "Bulding Updated Successfully", "response":bms_bulding_serializer.data})
            # return Response(bms_bulding_serializer.data) 
        return JsonResponse(bms_bulding_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bms_bulding.delete() 
        return JsonResponse({'message': 'Bulding was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



# Bms_floor_master crud Api

@api_view(['GET', 'POST', 'DELETE'])
def floor_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        bms_floor = Bms_floor_master.objects.all()
        bms_floor_serializer = Bms_floor_master_Serializer(bms_floor, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Floor Lists", "response":bms_floor_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        floor_serializer = Bms_floor_master_Serializer(data=request.data)
        # tutorial_serializer = Bms_floor_master_Serializer(data=tutorial_data)
        if floor_serializer.is_valid():
            floor_serializer.save()
            # print(tutorial_serializer.data)
            # return JsonResponse(floor_serializer.data, status=status.HTTP_201_CREATED) 
            return Response({"data":"true","status_code": "200", "message": "Floor Added Successfully", "response":floor_serializer.data})
            
        return JsonResponse(floor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_floor_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    


@api_view(['GET', 'PUT', 'DELETE'])
def floor_details(request, pk):
    try: 
        tutorial = Bms_floor_master.objects.get(pk=pk) 
    except Bms_floor_master.DoesNotExist: 
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_floor_master_Serializer(tutorial) 
        return Response({"data":"true","status_code": "200", "message": "Get Floor Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_serializer = Bms_floor_master_Serializer(tutorial, data=request.data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            # return JsonResponse(tutorial_serializer.data) 
            return Response({"data":"true","status_code": "200", "message": "Updated Floor Successfully", "response":tutorial_serializer.data}) 
            
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Floor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
 
 
    
# Bms_Deperament_master crud
   
@api_view(['GET', 'POST', 'DELETE'])
def department_list(request):
    if request.method == 'GET':
        bms_department = Bms_department_master.objects.all()    
        bms_department_serializer = Bms_department_master_Serializer(bms_department, many=True)
        # return JsonResponse(bms_department_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Departments Lists", "response":bms_department_serializer.data})
        
        
    elif request.method == 'POST':
        department_serializer = Bms_department_master_Serializer(data=request.data)
        # tutorial_serializer = Bms_department_master_Serializer(data=tutorial_data)
        if department_serializer.is_valid():
            department_serializer.save()
            # return JsonResponse(department_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"data":"true","status_code": "200", "message": "Department Added Successfully", "response":department_serializer.data})
             
        return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_department_master.objects.all().delete()
        return Response({'message': '{} Department deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def department(request, pk):
    try: 
        Bms_department = Bms_department_master.objects.get(pk=pk) 
    except Bms_department_master.DoesNotExist: 
        return Response({'message': 'Department does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        department_serializer = Bms_department_master_Serializer(Bms_department) 
        return Response({"data":"true","status_code": "200", "message": "Get data Successfully", "response":department_serializer.data}) 
 
    elif request.method == 'PUT':
        department_serializer = Bms_department_master_Serializer(Bms_department,data=request.data) 
        if department_serializer.is_valid(): 
            department_serializer.save() 
            # return JsonResponse(department_serializer.data) 
            return Response({"data":"true","status_code": "200", "message": "Update department Successfully", "response":department_serializer.data}) 
            
        return JsonResponse(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Bms_department.delete() 
        return JsonResponse({'message': 'Department deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
    
    
# Bms_sub_area_master crud


@api_view(['GET', 'POST', 'DELETE'])
def Bms_sub_area_list(request):
    if request.method == 'GET':
        bms_sub_area = Bms_sub_area_master.objects.all()
        bms_sub_area_serializer = Bms_sub_area_master_Serializer(bms_sub_area, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Sub_area Lists", "response":bms_sub_area_serializer.data})
        
        
    elif request.method == 'POST':
        sub_area_serializer = Bms_sub_area_master_Serializer(data=request.data)
        if sub_area_serializer.is_valid():
            sub_area_serializer.save()
            # return JsonResponse(sub_area_serializer.data, status=status.HTTP_201_CREATED) 
            return Response({"data":"true","status_code": "200", "message": "Sub Area Added Successfully", "response":sub_area_serializer.data})
            
        return Response(sub_area_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_sub_area_master.objects.all().delete()
        return JsonResponse({'message': '{} Sub_area deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def Bms_sub_area(request, pk):
    try: 
        bms_sub_area = Bms_sub_area_master.objects.get(pk=pk) 
    except Bms_sub_area_master.DoesNotExist: 
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bms_subarea_serializer = Bms_sub_area_master_Serializer(bms_sub_area) 
        return Response({"data":"true","status_code": "200", "message": "Get data Successfully", "response":bms_subarea_serializer.data}) 
 
    elif request.method == 'PUT': 
        bms_subarea_serializer = Bms_sub_area_master_Serializer(bms_sub_area, data=request.data) 
        if bms_subarea_serializer.is_valid(): 
            bms_subarea_serializer.save() 
            # return JsonResponse(bms_subarea_serializer.data) 
            return Response({"data":"true","status_code": "200", "message": "Update Sub Area Successfully", "response":bms_subarea_serializer.data}) 
        return Response(bms_subarea_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bms_sub_area.delete() 
        return Response({'message': 'Sub Area deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_locker crud
    

@api_view(['GET', 'POST', 'DELETE'])
def Bms_locker_list(request):
    if request.method == 'GET':
        bms_lockers = Bms_locker.objects.all()   
        locker_serializer = Bms_locker_Serializer(bms_lockers, many=True)
        return Response({"data":"true","status_code": "200", "message": "Locker Lists", "response":locker_serializer.data})
        
        
    elif request.method == 'POST':
        bms_locker_serializer = Bms_locker_Serializer(data=request.data)
        if bms_locker_serializer.is_valid():
            bms_locker_serializer.save()
            # return JsonResponse(bms_locker_serializer.data, status=status.HTTP_201_CREATED) 
            return Response({"data":"true","status_code": "200", "message": "Locker Added Successfully", "response":bms_locker_serializer.data})
        return Response(bms_locker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_locker.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def Bms_locker_list_details(request, pk):
    try: 
        bms_locker = Bms_locker.objects.get(pk=pk) 
    except Bms_locker.DoesNotExist: 
        return Response({'message': 'Locker does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        locker_serializer = Bms_locker_Serializer(bms_locker) 
        return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":locker_serializer.data}) 
 
    elif request.method == 'PUT': 
        locker_serializer = Bms_locker_Serializer(bms_locker, data=request.data) 
        if locker_serializer.is_valid(): 
            locker_serializer.save() 
            # return Response(locker_serializer.data) 
            return Response({"data":"true","status_code": "200", "message": "Update Locker Successfully", "response":locker_serializer.data}) 
        return Response(locker_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bms_locker.delete() 
        return Response({'message': 'locker was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# Device API LIST

@api_view(['GET', 'POST', 'PUT','DELETE'])
def Device_list(request):
    if request.method == 'GET':
        tutorials = Bms_device_information.objects.all()      
        tutorials_serializer = Bms_Devices_Serializer(tutorials, many=True)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
       
        
        
    elif request.method == 'POST':
        tutorial_serializer = Bms_Devices_Serializer(data=request.data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_device_information.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
    
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_Devices_Serializer(tutorial_data, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
    
   
# Device master api

# @api_view(['GET', 'POST', 'DELETE'])
# def Bms_device_list(request):
#     if request.method == 'GET':
#         # a=int(input('plese enter the password: '))
#         tutorials = Bms_device_master.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
        
#         tutorials_serializer = Bms_Device_master(tutorials, many=True)
#         # return JsonResponse(tutorials_serializer.data, safe=False)
#         return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
#         # 'safe=False' for objects serialization
        
        
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
    
#         # tutorial_serializer = TutorialSerializer(data=request.data)
#         tutorial_serializer = Bms_Device_master(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             # if not Tutorial.objects.filter(published=request.POST['published']).
#         # if tutorial_serializer==abc:
#             tutorial_serializer.save()
#             # print(tutorial_serializer.data)
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         count = Bms_device_master.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




# @api_view(['GET', 'PUT', 'DELETE'])
# def Bms_device_details(request, pk):
#     try: 
#         tutorial = Bms_device_master.objects.get(pk=pk) 
#     except Bms_device_master.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         tutorial_serializer = Bms_Device_master(tutorial) 
#         return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = Bms_Device_master(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)