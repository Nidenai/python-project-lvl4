from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # noqa

from .models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
