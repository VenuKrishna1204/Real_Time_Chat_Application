from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/personal_chat/(?P<room_name>\w+)/$', consumers.PersonalConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
