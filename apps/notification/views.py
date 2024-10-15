from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class NotificationView(LoginRequiredMixin, ListView):
    template_name = 'notification/notification-list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        notifications = NotificationModel.objects.filter(user=self.request.user)
        return notifications
