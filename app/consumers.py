from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from app.models import Message, Room


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('main', self.channel_name)
        self.accept()

    def receive(self, text_data):
        if len(text_data) < 1:
            return

        item = Message()
        item.room = Room.objects.filter(title='General').first()
        item.content = text_data
        item.save()

        async_to_sync(self.channel_layer.group_send)('main', {'type': 'message_created', 'content': text_data})


    def message_created(self, event):
        self.send(text_data=event['content'])
