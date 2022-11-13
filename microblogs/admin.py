"""configuration of administrative interface of microblogs"""

from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """configuration of admin interface for user class"""
    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active'
    ]
