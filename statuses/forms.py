from django import forms
from .models import *


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('id', 'name')