from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('logout', LogOutView.as_view(), name='logout'),
]