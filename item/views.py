from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from item.models import Item
from item.serializer import ItemSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def item(request):
    if request.method == 'GET':
        item = Item.objects.all()
        item_serializer = ItemSerializer(item, many=True)
        return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)