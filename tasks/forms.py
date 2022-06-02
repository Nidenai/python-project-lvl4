from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'mark')


class LabelForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ('id', 'label_name')