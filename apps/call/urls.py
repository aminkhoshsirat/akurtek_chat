from django.urls import path
from .views import *

app_name = 'call'


urlpatterns = [
    path('video-call', VideoCallView.as_view(), name='video-call')
]