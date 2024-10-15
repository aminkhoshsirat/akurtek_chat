from django.urls import re_path, path
from apps.notification.consumers import NotificationConsumer
from apps.chat.consumers import ChatConsumer, FileConsumer
from apps.call.consumers import VideoChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/notification/(?P<room_name>\w+)/$', NotificationConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    re_path(r'ws/file/(?P<room_name>\w+)/$', FileConsumer.as_asgi()),
    path('ws/videochat/', VideoChatConsumer.as_asgi())
]
