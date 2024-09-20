from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('sign-in', LoginView.as_view(), name='login'),
    path('sign-up', SignUpView.as_view(), name='sign_in'),
    path('logout', LogOutView.as_view(), name='logout'),
]
