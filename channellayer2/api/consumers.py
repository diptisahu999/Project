# Topic- Chat App with Static Group Name
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, chat

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print('Websocket Connected...', event)
        print("Channel layer..",self.channel_layer)
        print("Channel Name..",self.channel_name)
        
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name...", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            'self.group_name',
            self.channel_name
        )
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('Message received from Client...',event['text'])
        print("Type of message received from client...",type(event['text']))
        data=json.loads(event['text'])
        print(data)
        print("chat message",data['msg'])
        

        # Find group object
        group=Group.objects.get(name=self.group_name)



        # Cretae new chat object
        chats=chat(content=data['msg'],group=group)
        chats.save()

        async_to_sync(self.channel_layer.group_send)('self.group_name',{
            'type':'chat.message',
            'message':event['text']

        })

    def chat_message(self,event):
        print('Event',event)
        print('Actual Data',event['message'])

        self.send({
            'type':'websocket.send',
            'text':event['message']
        })



    def websocket_disconnect(self,event):
        print('Websocket Disconnected..',event)
        print("Channel layer..",self.channel_layer)
        print("Channel Name..",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'self.group_name',
            self.channel_name
        )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print('Websocket Connected...', event)
        print("Channel layer..",self.channel_layer)
        print("Channel Name..",self.channel_name)
        #group_Name=self.scope['url_route']['kwargs']['groupkaname']
        #print("Group Name..",group_Name)
        await self.channel_layer.group_add(
            'self.group_name',
            self.channel_name
        )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('Message received from Client...',event['text'])
        await self.channel_layer.group_send('self.group_name',{
            'type':'chat.message',
            'message':event['text']

        })

    async def chat_message(self,event):
        print('Event',event)
        print('Actual Data',event['message'])

        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })



    async def websocket_disconnect(self,event):
        print('Websocket Disconnected..',event)
        print("Channel layer..",self.channel_layer)
        print("Channel Name..",self.channel_name)
        await self.channel_layer.group_discard(
            'self.group_name',
            self.channel_name
        )
        raise StopConsumer()
        
        