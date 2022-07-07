from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass