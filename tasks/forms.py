from django import forms

from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('id', 'name', 'description', 'labels', 'status', 'executor')
