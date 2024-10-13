from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room, Message

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'url')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.SlugRelatedField(
        queryset=Room.objects.all(),
        slug_field='title',
    )
    # user = serializers.SlugRelatedField(
    #     queryset=User.objects.all(),
    #     slug_field='username',
    # )

    class Meta:
        model = Message
        fields = ('id', 'room', 'content')
