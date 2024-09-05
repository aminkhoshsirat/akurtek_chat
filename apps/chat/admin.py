from django.contrib import admin
from .models import *


@admin.register(ChatRoomModel)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['user1', 'user2']


@admin.register(ChatModel)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['room']


@admin.register(GroupRoomModel)
class GroupRoomAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GroupAdminModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['room']


@admin.register(GroupChatModel)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ['room']


@admin.register(ChannelRoomModel)
class ChannelRoomAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ChannelAdminModel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['room']


@admin.register(ChannelChatModel)
class ChannelChatAdmin(admin.ModelAdmin):
    list_display = ['room']
    