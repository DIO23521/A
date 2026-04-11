from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Anime, Genre, AnimeImage, Manga


# Create your views here.

class CatalogListView(ListView):
    queryset = Anime.objects.prefetch_related('genres')
    template_name = 'main/index.html'
    context_object_name = 'animes'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_genres'] = Genre.objects.all()

        search_query = self.request.GET.get('q')

        if search_query:
            context['animes'] = Anime.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

            context['mangas'] = Manga.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )
        else:
            context['mangas'] = Manga.objects.all()    
        return context

    


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'main/details.html'
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = self.object.images.all()

        if self.request.user.is_authenticated:
            context['user_likes_ids'] = self.request.user.user_likes.filter(
                anime__isnull=False).values_list('anime_id', flat=True)
            
        return context
    

    
class MangaDetailView(DetailView):
    queryset = Manga.objects.prefetch_related('adaptation')
    template_name = 'main/manga_details.html'
    context_object_name = 'manga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['m_gallery'] = self.object.m_images.all()

        if self.request.user.is_authenticated:
            context['user_likes_ids'] = self.request.user.user_likes.filter(
                manga__isnull=False).values_list('manga_id', flat=True)
            
        return context