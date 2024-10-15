from django.db import models
from apps.user.models import UserModel


class NotificationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_notification')
