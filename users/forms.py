from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name')


class UserList(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined')
