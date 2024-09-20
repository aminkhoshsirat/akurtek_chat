from django.contrib import admin
from .models import *


@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone']
