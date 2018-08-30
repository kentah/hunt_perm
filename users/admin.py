from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import HuntUserCreationForm, HuntUserChangeForm
from .models import HuntUser


class HuntUserAdmin(UserAdmin):
    add_form = HuntUserCreationForm
    form = HuntUserChangeForm
    model = HuntUser
    list_display = ['email', 'username']


admin.site.register(HuntUser, HuntUserAdmin)
