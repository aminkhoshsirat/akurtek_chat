import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
import urllib.parse as urlparse
from apps.user.models import UserModel
from asgiref.sync import sync_to_async
from .tasks import send_chat_file
from django.utils.timezone import now


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = self.room_name
        user = self.scope['user']
        await UserModel.objects.filter(id=user.id).aupdate(online=True)


        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        user = self.scope['user']
        await UserModel.objects.filter(id=user.id).aupdate(online=True)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        user = self.scope['user']
        message = data['message']
        type = data['type']
        query = self.scope['query_string'].decode('utf-8')
        params = urlparse.parse_qs(query)
        replay = params.get('replay_id', [None])[0]

        replay_object = await ChatModel.objects.filter(id=replay, room_id=self.room_group_name).afirst()

        if user.is_authenticated:
            if type == 'pv':
                await ChatModel.objects.acreate(room_id=self.room_group_name, sender=user,
                                                replay=replay_object, message=message)
                await ChatRoomModel.objects.filter(id=self.room_group_name).aupdate(last_message=message)

            elif type == 'group':
                await GroupChatModel.objects.acreate(room_id=self.room_group_name, sender=user,
                                                     message=message)
                await GroupRoomModel.objects.filter(id=self.room_group_name).aupdate(last_message=message)

            elif type == 'channel':
                await ChannelChatModel.objects.acreate(room_id=self.room_group_name, message=message, sender=user)
                await ChannelRoomModel.objects.filter(id=self.room_group_name).aupdate(last_message=message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))


class FileConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = self.room_name
        user = self.scope['user']
        await UserModel.objects.filter(id=user.id).aupdate(online=True)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        user = self.scope['user']
        await UserModel.objects.filter(id=user.id).aupdate(online=False)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        file = data["file"]
        print(data)
        name = str(data["name"]).replace('C:\\fakepath\\', '')
        user = self.scope['user']
        type = data['type']
        query = self.scope['query_string'].decode('utf-8')
        params = urlparse.parse_qs(query)
        replay = params.get('replay_id', [None])[0]
        replay_object = await ChatModel.objects.filter(id=replay, room_id=self.room_group_name).afirst()

        if user.is_authenticated:
            send_chat_file.delay(room_group_name=self.room_group_name, user=user.id,
                                 replay_object=replay_object, file=file, name=name, type=type)
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": name}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
