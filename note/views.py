from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from pymongo import MongoClient
from note.models import Note
from note.serializer import NoteSerializer
from note.mongoserializer import MongoSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def note(request):
    if request.method == 'GET':
        note = Note.objects.all()
        note_serializer = NoteSerializer(note, many=True)
        return JsonResponse(note_serializer.data, safe=False)
    elif request.method == 'POST':
        note_data = JSONParser().parse(request)
        note_serializer = NoteSerializer(data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def update(request, id):
    if request.method == 'GET':
        note = Note.objects.all()
        compras = note.filter(id=id)
        note_serializer = NoteSerializer(compras, many=True)
        return JsonResponse(note_serializer.data, safe=False)
    elif request.method == 'PUT':
        nota_data = JSONParser().parse(request)
        note = Note.objects.get(id=id)
        note_serializer = NoteSerializer(note, data=nota_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data)
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
