from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.AnimeListView.as_view(), name='home'),
    path('anime/<slug:slug>/', views.AnimeDetailView.as_view(), name='anime_detail')
]
