from django.urls import path

from app import consumers

ws_urlpatterns = [
    path('ws', consumers.ChatConsumer.as_asgi())
]
