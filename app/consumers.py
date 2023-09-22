# channels  version 3.0.4

from channels.consumer import SyncConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from . import models


class SyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connected", event)
        print(self.channel_name)
        print(self.channel_layer)
        # Add Group to channel
        self.groupname = self.scope["url_route"]["kwargs"]["groupkaname"]

        async_to_sync(self.channel_layer.group_add)(
            self.groupname, self.channel_name  # group name  # channel name
        )
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        async_to_sync(self.channel_layer.group_send)(
            self.groupname,  # group name
            {
                "type": "chat.message",
                "message": event["text"],
            },
        )
        message = event["text"]
        group = models.Group.objects.filter(name=self.groupname).first()
        chat = models.Chat.objects.create(content=message, group=group)
        chat.save()

        # print("message....", event["text"].message)

    def chat_message(self, event):
        print("Message", event)
        self.send(
            {
                "type": "websocket.send",
                "text": event["message"],
            }
        )

    def websocket_disconnect(self, event):
        print("Disconnected", event)
        async_to_sync(self.channel_layer.group_discard)(
            self.groupname, self.channel_name  # group name  # channel name
        )
