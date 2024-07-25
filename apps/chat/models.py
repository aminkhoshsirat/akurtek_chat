from django.db import models
from apps.user.models import UserModel
from django_jalali.db import models as jmodels


class ChatRoomModel(models.Model):
    user1 = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user1_rooms')
    user2 = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user2_rooms')
    date = jmodels.jDateTimeField()
    delete_user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, null=True, blank=True,
                                    related_name='users_delete_chats')


class ChatModel(models.Model):
    room = models.ForeignKey(ChatRoomModel, on_delete=models.DO_NOTHING, related_name='room_chats')
    message = models.TextField()
    sender = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_room_sender')
    delete_user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_room_deleter')
    date = jmodels.jDateTimeField(auto_now_add=True)
    edited = models.TextField(null=True, blank=True)
    last_message = models.TextField(null=True, blank=True)


class GroupRoomModel(models.Model):
    title = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='group/image')
    users = models.ManyToManyField(UserModel, related_name='user_groups')
    owner = models.ForeignKey(UserModel, models.DO_NOTHING, related_name='user_groups_owner')
    private = models.BooleanField(default=False)
    link = models.CharField(max_length=10000, unique=True)
    add_member = models.BooleanField(default=True)


class GroupAdminModel(models.Model):
    room = models.ForeignKey(GroupRoomModel, on_delete=models.CASCADE, related_name='group_admin')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='group_admin')
    can_add_admin = models.BooleanField(default=False)
    can_delete_message = models.BooleanField(default=False)
    can_change_info = models.BooleanField(default=False)
    can_add_user = models.BooleanField(default=True)


class GroupChatModel(models.Model):
    room = models.ForeignKey(GroupRoomModel, on_delete=models.CASCADE, related_name='group_chats')
    message = models.TextField()
    edited = models.TextField(null=True, blank=True)
    sender = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_group_sender')
    date = jmodels.jDateTimeField(auto_now_add=True)
    last_message = models.TextField(null=True, blank=True)


class ChannelRoomModel(models.Model):
    title = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='channel/image')
    users = models.ManyToManyField(UserModel, related_name='user_channels')
    owner = models.ForeignKey(UserModel, models.DO_NOTHING, related_name='user_channels_owner')
    private = models.BooleanField(default=False)
    link = models.CharField(max_length=10000, unique=True)
    add_member = models.BooleanField(default=True)


class ChannelAdminModel(models.Model):
    room = models.ForeignKey(ChannelRoomModel, on_delete=models.CASCADE, related_name='channel_admin')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='channel_admin')
    can_add_admin = models.BooleanField(default=False)
    can_delete_message = models.BooleanField(default=False)
    can_change_info = models.BooleanField(default=False)
    can_add_user = models.BooleanField(default=True)


class ChannelChatModel(models.Model):
    room = models.ForeignKey(GroupRoomModel, on_delete=models.CASCADE, related_name='channel_chats')
    message = models.TextField()
    edited = models.TextField(null=True, blank=True)
    sender = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_channel_sender')
    date = jmodels.jDateTimeField(auto_now_add=True)
    last_message = models.TextField(null=True, blank=True)
