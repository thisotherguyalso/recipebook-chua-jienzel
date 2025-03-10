"""Admin configuration for accounts app"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile
# Register your models here.


class ProfileInline(admin.StackedInline):
    """Profile inline model for user admin"""

    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    """User admin model with profile inline"""

    inlines = [ProfileInline, ]


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
