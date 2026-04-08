from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
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
        context['mangas'] = Manga.objects.all()
        context['animes'] = Anime.objects.all()
        return context

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'main/details.html'
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = self.object.images.all()
        return context
    
class MangaDetailView(DetailView):
    queryset = Manga.objects.prefetch_related('adaptation')
    template_name = 'main/manga_details.html'
    context_object_name = 'manga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['m_gallery'] = self.object.m_images.all()
        return context