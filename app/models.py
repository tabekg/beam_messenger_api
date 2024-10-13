# from django.conf import settings
from django.db import models

class Room(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    id = models.AutoField(primary_key=True)

    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    room = models.ForeignKey(Room, null=False, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
