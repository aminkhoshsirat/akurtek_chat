from django.db import models
from apps.user.models import UserModel


class ChatRoomModel(models.Model):
    user1 = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user1_rooms')
    user2 = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user2_rooms')
    date = models.DateTimeField()
    delete_user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, null=True, blank=True,
                                    related_name='users_delete_chats')
