from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from Authodication.models import Bms_Users
from Authodication.serializers import BmsUserDetailsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_Users.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = BmsUserDetailsSerializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response(tutorials_serializer.data)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = BmsUserDetailsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Users.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Bms_Users.objects.get(pk=pk) 
    except Bms_Users.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = BmsUserDetailsSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = BmsUserDetailsSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Bms_Users.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = BmsUserDetailsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
