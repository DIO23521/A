from django.contrib import admin
from . import models

# Register your models here.

class AnimeImageInLine(admin.TabularInline):
    model = models.AnimeImage
    extra = 1

@admin.register(models.Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['genres']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AnimeImageInLine]

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
