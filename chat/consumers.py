import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import datetime

class ChatConsumer(WebsocketConsumer):
    # websocket建立连接时执行方法
    def connect(self):
        # 从url里获取聊天室名字，为每个房间建立一个频道组
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # 将当前频道加入频道组
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        # 接受所有websocket请求
        self.accept()
    # websocket断开时执行方法
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Send message to WebSocket
        self.send(text_data=json.dumps({
             'message': f'{datetime_str}:{message}'
        }))