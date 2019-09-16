from django.shortcuts import get_object_or_404
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core import serializers
import json
import asyncio
##Sample Consumer-Devano Brown
class MessengerConsumer(AsyncJsonWebsocketConsumer):
    
    async def disconnect(self,close_code):
       pass

    async def checkActive(self):
        pass

    
    async def receive_json(self,content):
        pass
   
    
    #sample async function
    @database_sync_to_async
    def isUserAuthenticated(self,user):
        pass
        

