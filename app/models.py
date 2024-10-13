from django.conf import settings
from django.db import models

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Room(TimeStampMixin):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255, null=False)

class Message(TimeStampMixin):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(Room, null=False, on_delete=models.CASCADE)
    content = models.TextField()
