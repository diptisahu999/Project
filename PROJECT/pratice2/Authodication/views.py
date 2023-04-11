from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from Authodication.models import Bms_Roles,Bms_Users,Bms_Users_Details,Bms_Users_register,Bms_Module_master
from Authodication.serializers import BmsUserDetailsSerializer,RoleSerializer,UserSerializer,ModuleSerializer
from rest_framework.decorators import api_view
# from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate




class LoginView(APIView):
    def post(self,request,format=None):
        # tutorials = Bms_Users.objects.all()
        serializer=BmsUserDetailsSerializer(data=request.data)
        # serializer = BmsUserDetailsSerializer(tutorials, many=True)
        print(serializer)
        if serializer.is_valid():
            user_email=serializer.data.get('user_email')
            user_password=serializer.data.get('user_password')
            user=Bms_Users.objects.get(user_email=user_email,user_password=user_password)
            # user=authenticate(user_email=user_email,user_password=user_password)
            
            if user is not None:
                # token=get_tokens_for_user(user)
                return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":serializer.data})
            else:
                return Response({'error':{'non_field_error':['Email or password is not valid' ]}},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    
     

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_Users.objects.all()
        
        # title = request.GET.get('title', None)
        # if title is not None:
        #     tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = BmsUserDetailsSerializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
    
 
    elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = BmsUserDetailsSerializer(data=request.data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Users.objects.all().delete()
        return Response({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    try: 
        tutorial = Bms_Users.objects.get(pk=pk) 
    except Bms_Users.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = BmsUserDetailsSerializer(tutorial) 
        return Response(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        # tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = BmsUserDetailsSerializer(tutorial, data=request.data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def user_list_published(request):
    tutorials = Bms_Users.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = BmsUserDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)



    
# Role Table Api crud

# def get_tokens_for_user(user):                      # token generated function
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
   
@api_view(['GET', 'POST', 'DELETE'])
def role_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_Roles.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = RoleSerializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        # return Response(tutorials_serializer.data)
        return Response({"data":"true","status_code": "200", "message": "Role lists", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = RoleSerializer(data=request.data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            e=tutorial_serializer.save()
            # token=get_tokens_for_user(e)
            # print(tutorial_serializer.data)
            # return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"data":"true","status_code": "200", "message": "User role created Successfully!!","response":tutorial_serializer.data})
            # return Response({"data":"true","status_code": "200", "message": "User role created Successfully!!",'token':token, "response":tutorial_serializer.data})
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Roles.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    try: 
        tutorial = Bms_Roles.objects.get(pk=pk) 
    except Bms_Roles.DoesNotExist: 
        # return JsonResponse({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        return Response({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
 
    if request.method == 'GET': 
        tutorial_serializer = RoleSerializer(tutorial) 
        return Response(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        # tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = RoleSerializer(tutorial, data=request.data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "User Role updated Sucessfuly!!","response":tutorial_serializer.data}) 
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def role_list_published(request):
    tutorials = Bms_Roles.objects.filter(published=True)    
    
    if request.method == 'GET':
        tutorials_serializer = RoleSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
    
    
# Bms_Users_Details table crud

@api_view(['GET', 'POST', 'DELETE'])
def user_details_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_Users_Details.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = UserSerializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "User Lists", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = UserSerializer(data=request.data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": "200", "message": "User Added Sucessfuly!!","response":tutorial_serializer.data}) 
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Users_Details.objects.all().delete()
        return Response({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try: 
        tutorial = Bms_Users_Details.objects.get(pk=pk) 
    except Bms_Users_Details.DoesNotExist: 
        return Response({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        tutorial_serializer = UserSerializer(tutorial) 
        return Response(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        # tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = UserSerializer(tutorial, data=request.data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "User details updated Sucessfuly!!","response":tutorial_serializer.data}) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
         
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_Module crud



@api_view(['GET', 'POST', 'DELETE'])
def module_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_Module_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = ModuleSerializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "module Lists", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = ModuleSerializer(data=request.data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": "200", "message": "Module Added Sucessfuly!!","response":tutorial_serializer.data}) 
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Module_master.objects.all().delete()
        return Response({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def module_detail(request, pk):
    try: 
        tutorial = Bms_Module_master.objects.get(pk=pk) 
    except Bms_Module_master.DoesNotExist: 
        return Response({'message': 'The Module does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        tutorial_serializer = ModuleSerializer(tutorial) 
        return Response(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        # tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ModuleSerializer(tutorial, data=request.data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "Module updated Sucessfuly!!","response":tutorial_serializer.data}) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
         
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return Response({'message': 'Module was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



    
        

