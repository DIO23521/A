from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff']
    search_fields = ['username']
    fieldsets = UserAdmin.fieldsets + (
        ('optional info', {'fields': ('avatar', 'bio', 'birth_date')}),
    )