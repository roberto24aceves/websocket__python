import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class WaitingTurnConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "turns_%s" % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(self.room_group_name)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_message",
                "message": message,
            },
        )

    async def send_turns(self, event):
        turn_id = event["id"]
        turn_status = event["status"]
        await self.send(text_data=json.dumps({
            "id": turn_id,
            "status": turn_status,
        }))

    async def send_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))