from django import forms
from .models import *


class LabelForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ('id', 'label_name')