from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    list_display = []
