from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'description', 'mark')


class LabelForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ('label_name',)