from django import forms
from .models import *


class StatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ('id', 'status_name')