from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class NewContentAdmin(admin.ModelAdmin):
    exclude = ('created_user',)

    def save_model(self, request, obj, form, change):
        if not obk.pk:
            obj.created_user = request.user
        super().save_model(request, obj, form, change)