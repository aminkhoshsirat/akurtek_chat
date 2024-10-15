from django.db import models
from apps.user.models import UserModel
from django_jalali.db import models as jmodels


STATUS = {
    0: 'Connecting',
    1: 'Not Available',
    2: 'Accepted',
    3: 'Rejected',
    4: 'Busy',
    5: 'Processing',
    6: 'Ended'
}


class VideoCallModel(models.Model):
    caller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_caller')
    callee = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_callee')
    status = models.CharField(max_length=1000, choices=STATUS, default=0)
    date_started = jmodels.jDateTimeField()
    date_ended = jmodels.jDateTimeField()
    date_created = jmodels.jDateTimeField()