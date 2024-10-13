from django.shortcuts import render
from rest_framework import viewsets

from .serializers import RoomSerializer, MessageSerializer
from .models import Room, Message

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageSerializer


def home_page(request):
    return render(request, 'index.html')
