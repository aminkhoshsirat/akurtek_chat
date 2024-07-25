from django.shortcuts import render
from django.views.generic import View, ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.user.models import *
from apps.panel.models import SiteDetailModel
from .models import *


class IndexView(LoginRequiredMixin, View):
    login_url = '/user/login'
    def get(self, request):
        user = self.request.user
        rooms = ChatRoomModel.objects.filter(Q(user1=user) | Q(user2=user), ~Q(delete_user=user)).order_by('-date')
        group_rooms = GroupRoomModel.objects.filter(Q(users=user) | Q(owner=user))
        channel_rooms = GroupRoomModel.objects.filter(Q(users=user) | Q(owner=user))
        site_detail = SiteDetailModel.objects.first()
        context = {
            'rooms': rooms,
            'site_detail': site_detail,
            'group_rooms': group_rooms,
            'channel_rooms': channel_rooms,
        }
        return render(request, 'index.html', context)
