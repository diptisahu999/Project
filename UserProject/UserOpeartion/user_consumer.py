import json
from turtle import update
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from UserOpeartion.views import websocket_userAdd,get_user_list,websocket_update_user,websocket_delete_user


class UserConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "comp",
            self.channel_name
        )
        await self.accept()
        s = get_user_list()
        await self.channel_layer.group_send("comp", {
            'type': 'user_config',
            'response': s,
        })

    async def disconnect(self, close_code):
        self.channel_layer.group_discard("dash", self.channel_name)

    
    async def receive(self, text_data):
        # logging.info(text_data)        
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        print(response)
        # logging.info(response)

        if response['opr_type'] == 'user':
            if response['opr'] == 'add':
                websocket_userAdd(data=response['data'])
                s = get_user_list()
                await self.channel_layer.group_send("comp", {
                    'type': 'user_config',
                    'response': s,
                })
            elif response['opr'] == 'update':
                #  websocket_userAdd(data=response['data'])
                websocket_update_user(17,data=response['data'])
                s = get_user_list()
                # s=print_update_data(1)
                await self.channel_layer.group_send("comp", {
                    'type': 'user_config',
                    'response': s,
                })
                # update_user(data=response)
            elif response['opr'] == 'delete':
                websocket_delete_user(17)
                s = get_user_list()
                await self.channel_layer.group_send("comp", {
                    'type': 'user_config',
                    'response': s,
                })


    async def user_config(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "status_code": 200,
            "payload": res,
        }))   
    async def dataSender(self, data):
        self.channel_layer.group_send("dash", {
            'type': 'send_message',
            'response': data,
        })
                                                                               

# // CRC00003 16:22:23:883 : 0F 01 FE FF FE 00 31 01 3E 03 64 00 00 12 02
# // CRC00004 16:22:30:229 : 0F 01 FE FF FE 00 31 01 3E 02 00 00 00 23 1D
# // CRC00005 16:22:32:890 : 0F 01 FE FF FE 00 31 01 3E 03 00 00 00 55 A9
# // CRC00006 16:22:34:935 : 0F 01 FE FF FE 00 31 01 3E 04 00 00 00 04 84
# // CRC00007 16:22:40:976 : 0F 01 FE FF FE 00 31 01 3E 01 00 00 00 B8 C1
# // CRC00005 16:25:02:398 : 0F 01 FE FF FE 00 31 01 3E 02 64 00 00 64 B6
# // CRC00004 16:26:11:161 : 0F 01 FE FF FE 00 31 01 3E 03 64 00 00 12 02