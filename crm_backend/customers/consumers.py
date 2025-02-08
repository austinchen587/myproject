import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CustomerCommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("customer_comments", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("customer_comments", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "customer_comments",
            {
                "type": "comment_update",
                "customer_id": data["customer_id"],
                "customer_name": data["customer_name"],
            },
        )

    async def comment_update(self, event):
        await self.send(text_data=json.dumps(event))