from django.contrib import admin
from .models import *


@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone']


@admin.register(UserDeviceModel)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ['user', 'device_name', 'ip']


@admin.register(UserContactsModel)
class UserContactsAdmin(admin.ModelAdmin):
    list_display = ['user', 'to_user']


@admin.register(UserFavoriteModel)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'to_user']


@admin.register(UserGifModel)
class UserGifAdmin(admin.ModelAdmin):
    list_display = ['user', 'file']


@admin.register(UserFilesModel)
class UserFilesAdmin(admin.ModelAdmin):
    list_display = ['user', 'file', 'title', 'date']


@admin.register(UserStoryModel)
class UserStoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'file']
