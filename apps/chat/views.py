from django.shortcuts import render, Http404
from django.views.generic import View, ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.user.models import *
from apps.panel.models import SiteDetailModel
from .models import *
from itertools import chain
from django.utils.safestring import mark_safe


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        user = self.request.user
        rooms = ChatRoomModel.objects.filter(Q(user1=user) | Q(user2=user), ~Q(delete_user=user)).order_by('-date')
        group_rooms = GroupRoomModel.objects.filter(Q(users=user) | Q(owner=user))
        channel_rooms = GroupRoomModel.objects.filter(Q(users=user) | Q(owner=user))
        site_detail = SiteDetailModel.objects.first()
        rooms_list = sorted(
            chain(rooms, group_rooms, channel_rooms),
            key=lambda room: room.date, reverse=True)
        context = {
            'rooms': rooms,
            'site_detail': site_detail,
            'group_rooms': group_rooms,
            'channel_rooms': channel_rooms,
            'rooms_list': rooms_list
        }
        return render(request, 'index.html', context)


class ChatView(View):
    def get(self, request, id):
        user = self.request.user
        if user.is_authenticated:
            chat_room = ChatRoomModel.objects.filter(id=id).first()
            if chat_room and (chat_room.user1 == user or chat_room.user2 == user):
                context = {
                    'chats': ChatModel.objects.filter(room=chat_room).order_by('-date')[::-1],
                    'room_id': mark_safe(chat_room.id),
                    'room': chat_room
                }
                return render(request, 'chat/chat.html', context)
        return Http404
