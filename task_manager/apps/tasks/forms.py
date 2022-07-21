from django import forms

from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('id', 'name', 'description', 'status', 'executor', 'labels')
