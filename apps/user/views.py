from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views.generic import View
from apps.panel.models import SiteDetailModel
from redis import Redis
from .models import *


re = Redis(host='localhost', db=8)


class LoginView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.first()
        UserModel.objects.create_user(phone='09909795332', fullname='amin kh', password='')
        context = {
            'site_detail': site_detail,
        }
        return render(request, 'user/login.html', context)


class LogOutView(LogoutView):
    pass
