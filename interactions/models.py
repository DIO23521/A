from django.db import models
from django.conf import settings
from main.models import Anime, Manga

# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_likes')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='anime_likes', null=True, blank=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='manga_likes', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'anime', 'manga')
    
    def __str__(self):
        if self.manga:
            return f'{self.user.username} liked {self.manga.title}'
        elif self.anime:
            return f'{self.user.username} liked {self.anime.title}'
        return f'like form {self.user.username}'