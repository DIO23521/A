from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.

class AnimeImageInLine(admin.TabularInline):
    model = models.AnimeImage
    readonly_fields = ['thumbnail']
    extra = 1

    def thumbnail(self, instance):
        if instance.image.name != '':
            return mark_safe(f'<img src="{instance.image.url}" class="thumbnail" style="width: 50px; height: auto;" />')

class MangaImageInLine(admin.TabularInline):
    model = models.MangaImage
    readonly_fields = ['thumbnail']
    extra = 1

    def thumbnail(self, instance):
        if instance.image.name != '':
            return mark_safe(f'<img src="{instance.image.url}" class="thumbnail" style="width: 50px; height: auto;" />')
        return ''


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['genres']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AnimeImageInLine]


@admin.register(models.Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['genres']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MangaImageInLine]