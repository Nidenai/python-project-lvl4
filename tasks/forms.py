from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'label', 'status', 'created_user', 'assigned_user')
