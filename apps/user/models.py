from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MinLengthValidator
from utils import phone_codes


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone, fullname, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone:
            raise ValueError(_("The phone must be set"))
        user = self.model(phone=phone, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, fullname, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, fullname, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True)
    country = models.CharField(max_length=10000, choices=phone_codes)
    fullname = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['fullname']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


class Mode(models.Choices):
    all = 'all'
    contacts = 'contacts'
    no_one = 'no_one'


class UserModel(CustomUser):
    ban = models.BooleanField(default=False)
    profile_image = models.ImageField('user/profiles', blank=True, null=True)
    register_date = jmodels.jDateTimeField(auto_now_add=True)
    last_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_seen = models.ManyToManyField('UserModel', related_name='user_allow_seen')
    add_group = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_add_group = models.ManyToManyField('UserModel', related_name='user_allow_group_add')
    add_channel = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_add_channel = models.ManyToManyField('UserModel', related_name='user_allow_channel_add')
    profile_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_profile_seen = models.ManyToManyField('UserModel', related_name='user_allow_profile_seen')
    bio = models.CharField(max_length=10000)
    bio_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_seen_bio = models.ManyToManyField('UserModel', related_name='user_allow_bio_seen')
    story_seen = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    users_allowed_seen_story = models.ManyToManyField('UserModel', related_name='user_allow_story_seen')
    find_with_phone = models.CharField(max_length=1000, choices=Mode, default=Mode.all)
    birth_date = jmodels.jDateTimeField(null=True, blank=True)
    report = models.DateTimeField(null=True, blank=True)
    contacts = models.ManyToManyField('UserModel', related_name='user_contacts')
    favorite_contacts = models.ManyToManyField('UserModel', related_name='user_favorite_contacts')

    def __str__(self):
        return f'{self.phone} - {self.fullname}'


class UserDeviceModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)
    date = jmodels.jDateTimeField(auto_now_add=True)


class UserStoryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user/story')
