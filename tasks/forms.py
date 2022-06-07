from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'label', 'status', 'assigned_user', 'created_user')
