from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'anime', 'manga', 'created_at']
    search_fields = ['user']
    autocomplete_fields = ['anime', 'manga', 'user']