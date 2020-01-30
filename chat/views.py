from django.shortcuts import render
from django.views import View
import json

class ChatView(View):
    chat_templates_name= 'chat/index.html'
    room_templates_name= 'chat/room.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, **kwargs):

        if request.resolver_match.url_name == 'index':
            return render(request, self.chat_templates_name,{})

        if request.resolver_match.url_name == 'room':
            room = kwargs['room']
            return render(request, self.room_templates_name,{'room':room})