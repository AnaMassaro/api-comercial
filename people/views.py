from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib import auth
from people.models import People
from people.serializer import PeopleSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def helloworld(request):
    if request.method == 'GET':
        list = {'mensagem':'hello world'}
        return JsonResponse(list, safe=False, status=status.HTTP_200_OK)



@api_view(['GET', 'POST'])
def user(request):
    if request.method == 'GET':
        people = People.objects.all()
        people_serializer = PeopleSerializer(people, many=True)
        return JsonResponse(people_serializer.data, safe=False)
    elif request.method == 'POST':
        people_data = JSONParser().parse(request)
        people_serializer = PeopleSerializer(data=people_data)
        if people_serializer.is_valid():
            people_serializer.save()
            return JsonResponse(people_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(people_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

