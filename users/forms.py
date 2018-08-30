from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import HuntUser


class HuntUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = HuntUser
        fields = ('username', 'email')


class HuntUserChangeForm(UserChangeForm):

    class Meta:
        model = HuntUser
        fields = ('username', 'email')
