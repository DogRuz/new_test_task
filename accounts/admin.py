from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ['username', 'phone', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )  # this will allow to change these fields in admin module


admin.site.register(User, MyUserAdmin)
