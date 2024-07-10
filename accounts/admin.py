from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined'
    ordering = 'date_joined',
