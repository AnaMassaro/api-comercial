from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from noteItem.models import NoteItem
from noteItem.serializer import NoteItemSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def rota(request):
    if request.method == 'GET':
        noteitem = NoteItem.objects.all()
        noteitem_serializer = NoteItemSerializer(noteitem, many=True)
        return JsonResponse(noteitem_serializer.data, safe=False)
    elif request.method == 'POST':
        noteitem_data = JSONParser().parse(request)
        noteitem_serializer = NoteItemSerializer(data=noteitem_data)
        if noteitem_serializer.is_valid():
            noteitem_serializer.save()
            return JsonResponse(noteitem_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(noteitem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, id):
    if request.method == 'GET':
        note = NoteItem.objects.all()
        compras = note.filter(note=id)
        note_serializer = NoteItemSerializer(compras, many=True)
        return JsonResponse(note_serializer.data, safe=False)