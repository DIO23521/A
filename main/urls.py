from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path('', views.CatalogListView.as_view(), name='home'),
    path('anime/<slug:slug>/', views.AnimeDetailView.as_view(), name='anime_detail'),
    path('manga/<slug:slug>/', views.MangaDetailView.as_view(), name='manga_detail')
]
