from django.db import models
from django_jalali.db import models as jmodels


class Mode(models.Choices):
    all = 'all'
    contacts = 'contacts'
    no_one = 'no_one'


class UserModel(models.Model):
    profile_image = models.ImageField()
    last_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_seen = models.ManyToManyField('UserModel')
    add_group = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_add_group = models.ManyToManyField('UserModel')
    add_channel = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_add_channel = models.ManyToManyField('UserModel')
    profile_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_profile_seen = models.ManyToManyField('UserModel')
    bio = models.CharField(max_length=10000)
    bio_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_seen_bio = models.ManyToManyField('UserModel')
    story_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_seen_story = models.ManyToManyField('UserModel')
    find_with_phone = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    birth_date = jmodels.jDateTimeField(null=True, blank=True)
    report = models.DateTimeField(null=True, blank=True)


class UserContactsModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    contact = models.ManyToManyField(UserModel)
    phone = models.CharField(max_length=20)


class UserFavoriteContactsModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    contact = models.ManyToManyField(UserModel)


class UserDeviceModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)
    date = jmodels.jDateTimeField(auto_now_add=True)


class UserStoryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user/story')
