from django.urls import path
from .views import *

app_name = 'notification'

urlpatterns = [
    path('', NotificationView.as_view(), name='index'),
]