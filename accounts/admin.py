from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['username', 'email', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']

    fieldsets = ((None, {'fields': ('name',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name', )}),)


admin.site.register(CustomUser, CustomUserAdmin)
