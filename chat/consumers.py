import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


#等同于django的views.py
#对于channels叫consumers.py
#下面的内容作用：将新的ws客户端加入到一个频道，将其发送到ws服务端的内容广播至频道所有人
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            'chat',
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            'chat',
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        message = text_data
        # await self.send(text_data=json.dumps(text_data))
        # Send message to room group
        await self.channel_layer.group_send(
            'chat',
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

