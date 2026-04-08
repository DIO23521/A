from django.db import models
from django.utils.text import slugify

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    def save(self,  *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']



class Manga(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='main_manga_poster/', null=True, blank=True)
    adaptation = models.ManyToManyField('Anime', blank=True)
    genres = models.ManyToManyField(Genre)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    
class MangaImage(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='m_images')
    image = models.ImageField(upload_to='manga_images/', null=True, blank=True)



class Anime(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='main_posters/', null=True, blank=True)
    source = models.ForeignKey(
        'Manga', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    genres = models.ManyToManyField(Genre)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    

class AnimeImage(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)