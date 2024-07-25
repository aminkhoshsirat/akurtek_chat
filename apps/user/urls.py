from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),
]
